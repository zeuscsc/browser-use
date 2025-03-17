import logging
from browser_use import BrowserConfig
from fastapi import FastAPI, Request, HTTPException, Depends
from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.signature import SignatureVerifier
from browser_use.agent.service import Agent, Browser
from langchain_core.language_models.chat_models import BaseChatModel
from browser_use.logging_config import setup_logging

load_dotenv()

setup_logging()
logger = logging.getLogger('slack')

app = FastAPI()

class SlackBot:
    def __init__(self, llm: BaseChatModel, bot_token: str, signing_secret: str, ack: bool = False, browser_config: BrowserConfig = BrowserConfig(headless=True)):
        if not bot_token or not signing_secret:
            raise ValueError("Bot token and signing secret must be provided")
        
        self.llm = llm
        self.ack = ack
        self.browser_config = browser_config
        self.client = AsyncWebClient(token=bot_token)
        self.signature_verifier = SignatureVerifier(signing_secret)
        self.processed_events = set()
        logger.info("SlackBot initialized")

    async def handle_event(self, event, event_id):
        try:
            logger.info(f"Received event id: {event_id}")
            if not event_id:
                logger.warning("Event ID missing in event data")
                return

            if event_id in self.processed_events:
                logger.info(f"Event {event_id} already processed")
                return
            self.processed_events.add(event_id)

            if 'subtype' in event and event['subtype'] == 'bot_message':
                return

            text = event.get('text')
            user_id = event.get('user')
            if text and text.startswith('$bu '):
                task = text[len('$bu '):].strip()
                if self.ack:
                    try:
                        await self.send_message(event['channel'], f'<@{user_id}> Starting browser use task...', thread_ts=event.get('ts'))
                    except Exception as e:
                        logger.error(f"Error sending start message: {e}")

                try:
                    agent_message = await self.run_agent(task)
                    await self.send_message(event['channel'], f'<@{user_id}> {agent_message}', thread_ts=event.get('ts'))
                except Exception as e:
                    await self.send_message(event['channel'], f'Error during task execution: {str(e)}', thread_ts=event.get('ts'))
        except Exception as e:
            logger.error(f"Error in handle_event: {str(e)}")

    async def run_agent(self, task: str) -> str:
        try:
            browser = Browser(config=self.browser_config)
            agent = Agent(task=task, llm=self.llm, browser=browser)
            result = await agent.run()

            agent_message = None
            if result.is_done():
                agent_message = result.history[-1].result[0].extracted_content

            if agent_message is None:
                agent_message = 'Oops! Something went wrong while running Browser-Use.'

            return agent_message

        except Exception as e:
            logger.error(f"Error during task execution: {str(e)}")
            return f'Error during task execution: {str(e)}'

    async def send_message(self, channel, text, thread_ts=None):
        try:
            await self.client.chat_postMessage(channel=channel, text=text, thread_ts=thread_ts)
        except SlackApiError as e:
            logger.error(f"Error sending message: {e.response['error']}")

@app.post("/slack/events")
async def slack_events(request: Request, slack_bot: SlackBot = Depends()):
    try:
        if not slack_bot.signature_verifier.is_valid_request(await request.body(), dict(request.headers)):
            logger.warning("Request verification failed")
            raise HTTPException(status_code=400, detail="Request verification failed")

        event_data = await request.json()
        logger.info(f"Received event data: {event_data}")
        if 'challenge' in event_data:
            return {"challenge": event_data['challenge']}

        if 'event' in event_data:
            try:
                await slack_bot.handle_event(event_data.get('event'), event_data.get('event_id'))
            except Exception as e:
                logger.error(f"Error handling event: {str(e)}")

        return {}
    except Exception as e:
        logger.error(f"Error in slack_events: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")