import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent
from browser_use.llm import ChatOpenAI

llm = ChatOpenAI(model='gpt-4.1')

initial_actions = [
	{'go_to_url': {'url': 'https://www.google.com', 'new_tab': True}},
	{'go_to_url': {'url': 'https://en.wikipedia.org/wiki/Randomness', 'new_tab': True}},
	{'scroll_down': {'amount': 1000}},
]
agent = Agent(
	task='What theories are displayed on the page?',
	initial_actions=initial_actions,
	llm=llm,
)


async def main():
	await agent.run(max_steps=10)


if __name__ == '__main__':
	asyncio.run(main())
