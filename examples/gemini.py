import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))


async def run_search():
	agent = Agent(
		task=(
			# 'Go to url r/LocalLLaMA subreddit and search for "browser use" in the search bar and click on the first post and find the funniest comment'
			"""Go to HSBC.com.hk then under the borrowing cards & loans tab there is a Compare Credit Cards option. Click on it and select: 
			Premier MasterCard, Red Credit Card and EveryMile Credit Card. 
			You many need to keep scrolling down to see the all cards, the Compare button is at the bottom.
			Then select the Compare button and summarize the difference of each card in zh-tw.
			"""
		),
		llm=llm,
		max_actions_per_step=4,
		tool_call_in_content=False,
	)

	await agent.run(max_steps=25)


if __name__ == '__main__':
	asyncio.run(run_search())
