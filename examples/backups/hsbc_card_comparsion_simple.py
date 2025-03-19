import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent
from browser_use import Agent, Browser, Controller,BrowserConfig
from browser_use.browser.context import BrowserContextConfig
import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

TASK="""Go to https://www.hsbc.com.hk/credit-cards/compare/
Click the 'Add Card' Buttons, scroll down the list if needed.
Find the 'EveryMile Credit Card' and 'Red Credit Card'
Click and Select it and then click Compare after you select the cards.
Save the differences from tables below:
~~~
At a glance
Welcome offers
Rewards
Travel privileges
Dining privileges
What else could you enjoy?
Can you apply?
Important information
~~~
Read through all the differences until the end of the page (When you see Back to Top)."""
browser = Browser(
	config=BrowserConfig(
		headless=False,  # This is True in production
		disable_security=True,
		new_context_config=BrowserContextConfig(
			disable_security=True,
			minimum_wait_page_load_time=1,  # 3 on prod
			maximum_wait_page_load_time=10,  # 20 on prod
			# no_viewport=True,
			browser_window_size={
				'width': 2560,
				'height': 1600,
			},
			# trace_path='./tmp/web_voyager_agent',
		),
	)
)
async def main():
	agent = Agent(
		task=TASK,
		llm=llm,
		browser=browser,
		validate_output=True,
	)
	history = await agent.run(max_steps=50)
	history.save_to_file('./tmp/history.json')
	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())
