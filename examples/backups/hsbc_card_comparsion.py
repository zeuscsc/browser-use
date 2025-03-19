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


async def main():

	config=BrowserConfig(
		headless=False,  # This is True in production
		disable_security=True,
		)
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
		)
	browser = Browser(config=config)
	async with await browser.new_context(config=new_context_config) as context:
		model = llm
		agent_pick_cards = Agent(
			task="""Go to https://www.hsbc.com.hk/credit-cards/compare/
Click the 'Add Card' Buttons, scroll down the list if needed.
Find the 'EveryMile Credit Card' and 'Red Credit Card'
Click and Select it and then click Compare after you select the cards.""",
			llm=model,
			browser_context=context,
		)
		agent_table_1 = Agent(
			task="""Scroll Down Until' At a glance' Table, extract the differences""",
			llm=model,
			browser_context=context,
		)
		agent_table_2 = Agent(
			task="""Scroll Down Until 'Welcome offers' Table, extract the differences""",
			llm=model,
			browser_context=context,
		)
		agent_table_3 = Agent(
			task="""Scroll Down Until 'Rewards' Table, extract the differences""",
			llm=model,
			browser_context=context,
		)
		agent_table_4 = Agent(
			task="""Scroll Down Until 'Travel privileges' Table, extract the differences""",
			llm=model,
			browser_context=context,
		)
		agent_end = Agent(
			task="""Read through all the differences until the end of the page (When you see Back to Top).""",
			llm=model,
			browser_context=context,
		)
		history=await agent_pick_cards.run(max_steps=10);history.save_to_file("./tmp/hsbc_card_comparsion_multi_agent/agent_pick_cards.json");os.rename("agent_history.gif","./tmp/hsbc_card_comparsion_multi_agent/agent_pick_cards.gif")
		history=await agent_table_1.run(max_steps=3);history.save_to_file("./tmp/hsbc_card_comparsion_multi_agent/agent_table_1.json");os.rename("agent_history.gif","./tmp/hsbc_card_comparsion_multi_agent/agent_table_1.gif")
		history=await agent_table_2.run(max_steps=3);history.save_to_file("./tmp/hsbc_card_comparsion_multi_agent/agent_table_2.json");os.rename("agent_history.gif","./tmp/hsbc_card_comparsion_multi_agent/agent_table_2.gif")
		history=await agent_table_3.run(max_steps=3);history.save_to_file("./tmp/hsbc_card_comparsion_multi_agent/agent_table_3.json");os.rename("agent_history.gif","./tmp/hsbc_card_comparsion_multi_agent/agent_table_3.gif")
		history=await agent_table_4.run(max_steps=3);history.save_to_file("./tmp/hsbc_card_comparsion_multi_agent/agent_table_4.json");os.rename("agent_history.gif","./tmp/hsbc_card_comparsion_multi_agent/agent_table_4.gif")
		history=await agent_end.run(max_steps=3);history.save_to_file("./tmp/hsbc_card_comparsion_multi_agent/agent_end.json");os.rename("agent_history.gif","./tmp/hsbc_card_comparsion_multi_agent/agent_end.gif")


if __name__ == '__main__':
	asyncio.run(main())
