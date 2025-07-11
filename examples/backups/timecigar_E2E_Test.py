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
import time
import shutil


load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

current_path = Path(__file__).parent
root_path = current_path.parent
history_path=os.path.join(os.path.dirname(__file__),"tmp","timecigar_E2E_Test")
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

def backup_gif(dir_path, gif_name, root_path=".", timeout=10, polling_interval=0.5):
    """
    Backs up a GIF file, ensuring it exists before renaming.

    Args:
        dir_path: The directory to save the backup GIF.
        gif_name: The desired name for the backup GIF (without .gif extension).
        root_path: The root directory where agent_history.gif might be located. Defaults to the current directory.
        timeout: Maximum time (in seconds) to wait for the GIF to appear.
        polling_interval: Time (in seconds) between checks for the GIF's existence.
    """

    gif_path = "agent_history.gif"
    backup_path = os.path.join(dir_path, f"{gif_name}.gif")
    source_path = ""

    # Remove old backup if it exists
    if os.path.exists(backup_path):
        os.remove(backup_path)

    # Wait for the GIF to appear
    start_time = time.time()
    gif_found = False
    while time.time() - start_time < timeout:
        if os.path.exists(gif_path):
            source_path = gif_path
            gif_found = True
            break
        elif os.path.exists(os.path.join(root_path,gif_path)):
            source_path = os.path.join(root_path,gif_path)
            gif_found = True
            break
        time.sleep(polling_interval)

    if not gif_found:
        print(f"Warning: {gif_path} did not appear within {timeout} seconds.")
        return

    # Now that the GIF exists, attempt to rename it (using shutil.move for robustness)
    try:
        shutil.move(source_path, backup_path)  
    except Exception as e:
        print(f"Error renaming GIF: {e}")

async def main():
    config=BrowserConfig(
        headless=False,  # This is True in production
        disable_security=True,
    )
    new_context_config=BrowserContextConfig(
        disable_security=True,
        minimum_wait_page_load_time=5,  # 3 on prod
        maximum_wait_page_load_time=30,  # 20 on prod
        # no_viewport=True,
        browser_window_size={
            'width': 412,
            'height': 915,
        },
        # trace_path='./tmp/web_voyager_agent',
    )
    browser = Browser(config=config)
    async with await browser.new_context(config=new_context_config) as context:
        model = llm
        agent_visit_home_page = Agent(
            task="""Go to https://www.timecigar.com/
Accept the cookies (if any) and Conform the age limit dialog.
Scroll through the page and add some items to the cart.
""",
            llm=model,
            browser_context=context,
        )
        agent_gather_actions = Agent(
            task="""
Ggo to the shopping cart and see if all the prices and the total pcices is displayed correctly.
""",
            llm=model,
            browser_context=context,
        )
        history=await agent_visit_home_page.run(max_steps=10);history.save_to_file(f"{history_path}/agent_visit_home_page.json");backup_gif(history_path,"agent_visit_home_page")
        history=await agent_gather_actions.run(max_steps=10);history.save_to_file(f"{history_path}/agent_gather_actions.json");backup_gif(history_path,"agent_gather_actions")
        
        extracted_content=history.extracted_content()
        final_result=history.final_result()
        print(extracted_content)
        print(final_result)
        # actions_list=model.invoke(f"Extract the list from the actions description:{final_result}")
        # print(actions_list)

if __name__ == '__main__':
	asyncio.run(main())
