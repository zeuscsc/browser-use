import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY', '')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')


async def run_agent(task: str, max_steps: int = 38):
	llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', api_key=SecretStr(api_key))
	agent = Agent(task=task, llm=llm)
	result = await agent.run(max_steps=max_steps)
	return result
