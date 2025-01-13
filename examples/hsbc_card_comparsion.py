import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent
from browser_use import Agent, Browser, Controller
from browser_use.browser.context import BrowserContextConfig

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))


async def main():

	browser = Browser()
	async with await browser.new_context() as context:
		model = llm
		agent_goto_hsbc = Agent(
			task='Go to https://www.hsbc.com.hk/credit-cards/compare/',
			llm=model,
			browser_context=context,
		)
		agent_select_card_1 = Agent(
			task="""Click the First 'Add Card' Button, scroll down the list until you reach 'Visa Gold Card for Students'.
			Click and Select it and then click Compare""",
			llm=model,
			browser_context=context,
		)
		agent_select_card_2 = Agent(
			task="""Click the Second 'Add Card' Button, scroll down the list until you reach 'Visa Platinum Card'.
			Click and Select it and then click Compare""",
			llm=model,
			browser_context=context,
		)
		agent_select_card_3 = Agent(
			task="""Click the Third 'Add Card' Button, scroll down the list until you reach 'Red Credit Card'.
			Click and Select it and then click Compare""",
			llm=model,
			browser_context=context,
		)
		agent_select_card_4 = Agent(
			task="""Click the Fourth 'Add Card' Button, scroll down the list until you reach 'EveryMile Credit Card'.
			Click and Select it and then click Compare""",
			llm=model,
			browser_context=context,
		)
		try:
			await agent_goto_hsbc.run()
		except Exception as e:
			pass
		await agent_select_card_1.run()
		await agent_select_card_2.run()
		await agent_select_card_3.run()
		await agent_select_card_4.run()


if __name__ == '__main__':
	asyncio.run(main())
