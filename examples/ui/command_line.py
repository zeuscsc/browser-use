"""
To Use It:

Example 1: Using OpenAI (default), with default task: 'go to reddit and search for posts about browser-use'
python command_line.py

Example 2: Using OpenAI with a Custom Query
python command_line.py --query "go to google and search for browser-use"

Example 3: Using Anthropic's Claude Model with a Custom Query
python command_line.py --query "find latest Python tutorials on Medium" --provider anthropic

"""
import os
import sys
import argparse
import asyncio

# Ensure local repository (browser_use) is accessible
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller


load_dotenv()

def get_llm(provider: str):
	if provider == 'anthropic':
		from langchain_anthropic import ChatAnthropic
		api_key = os.getenv("ANTHROPIC_API_KEY")
		if not api_key:
			raise ValueError("Error: ANTHROPIC_API_KEY is not set. Please provide a valid API key.")
        
		return ChatAnthropic(
			model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0
		)
	elif provider == 'openai':
		from langchain_openai import ChatOpenAI
		api_key = os.getenv("OPENAI_API_KEY")
		if not api_key:
			raise ValueError("Error: OPENAI_API_KEY is not set. Please provide a valid API key.")
        
		return ChatOpenAI(model='gpt-4o', temperature=0.0)

	else:
		raise ValueError(f'Unsupported provider: {provider}')

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Automate browser tasks using an LLM agent.")
    parser.add_argument(
        '--query',
        type=str,
        help='The query to process',
        default='go to reddit and search for posts about browser-use'
    )
    parser.add_argument(
        '--provider',
        type=str,
        choices=['openai', 'anthropic'],
        default='openai',
        help='The model provider to use (default: openai)',
    )
    return parser.parse_args()

def initialize_agent(query: str, provider: str):
    """Initialize the browser agent with the given query and provider."""
    llm = get_llm(provider)
    controller = Controller()
    browser = Browser(config=BrowserConfig())

    return Agent(
        task=query,
        llm=llm,
        controller=controller,
        browser=browser,
        use_vision=True,
        max_actions_per_step=1,
    ), browser

async def main():
    """Main async function to run the agent."""
    args = parse_arguments()
    agent, browser = initialize_agent(args.query, args.provider)

    await agent.run(max_steps=25)
    
    input('Press Enter to close the browser...')
    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())