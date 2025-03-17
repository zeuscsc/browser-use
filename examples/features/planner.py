import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent


llm = ChatOpenAI(model='gpt-4o', temperature=0.0)
planner_llm = ChatOpenAI(
	model='o3-mini',
)
task = 'your task'


agent = Agent(task=task, llm=llm, planner_llm=planner_llm, use_vision_for_planner=False, planner_interval=1)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
