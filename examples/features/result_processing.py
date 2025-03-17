import os
import sys
from pprint import pprint

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import (
	BrowserContext,
	BrowserContextConfig,
	BrowserContextWindowSize,
)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.controller.service import Controller

llm = ChatOpenAI(model='gpt-4o')
browser = Browser(
	config=BrowserConfig(
		headless=False,
		disable_security=True,
		extra_chromium_args=['--window-size=2000,2000'],
	)
)


async def main():
	async with await browser.new_context(
		config=BrowserContextConfig(
			trace_path='./tmp/result_processing',
			no_viewport=False,
			browser_window_size=BrowserContextWindowSize(width=1280, height=1000),
		)
	) as browser_context:
		agent = Agent(
			task="go to google.com and type 'OpenAI' click search and give me the first url",
			llm=llm,
			browser_context=browser_context,
		)
		history: AgentHistoryList = await agent.run(max_steps=3)

		print('Final Result:')
		pprint(history.final_result(), indent=4)

		print('\nErrors:')
		pprint(history.errors(), indent=4)

		# e.g. xPaths the model clicked on
		print('\nModel Outputs:')
		pprint(history.model_actions(), indent=4)

		print('\nThoughts:')
		pprint(history.model_thoughts(), indent=4)
	# close browser
	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())
