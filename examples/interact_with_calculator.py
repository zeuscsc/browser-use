import asyncio
import os
from typing import Any, Coroutine
import re
import pandas as pd
from tqdm import tqdm

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent, AgentHistoryList
from browser_use import Agent, Browser, Controller,BrowserConfig
from browser_use.browser.context import BrowserContextConfig
import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult, AgentState

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

from pydantic import BaseModel
from typing import List, Dict, Any, Optional


load_dotenv()
google_api_key = os.getenv('GEMINI_API_KEY')
open_router_api_key = os.getenv('OPEN_ROUTER_API_KEY')
if not google_api_key:
	raise ValueError('GEMINI_API_KEY is not set')
if not open_router_api_key:
    raise ValueError('OPEN_ROUTER_API_KEY is not set')

agent_llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(google_api_key))
planner_llm = ChatOpenAI(
			base_url='https://openrouter.ai/api/v1',
            model="deepseek/deepseek-r1",
            api_key=SecretStr(open_router_api_key))

PROJECT_NAME="hsbc_loan_comparsion"
BANK="HASE"
BANK_URL_MAPPING={
        "HASE":"https://www.hangseng.com/en-hk/personal/loans/instalment-loan/",
        "BoC":"https://www.bochk.com/dam/loans/personal/instalmentloan/tc.html",
        "SC":"https://www.sc.com/hk/loans/personal-instalment-loan/"
    }
# 50,000, 100,000 200,000 300,000 500,000 800,000 1,000,000 1,500,000
loan_amount_list=[50000,100000,200000,300000,500000,800000,1000000,1500000]
# 12 months, 24 months, 36 months, 60 months
period_list=[12,24,36,60]

class Snapshot(BaseModel):
	loan_amount: int
	period: int
	flat_rate: float
	annualised_percentage_rate: int


class Snapshots(BaseModel):
	snapshots: List[Snapshot]
controller = Controller(output_model=Snapshots)

initial_actions = [
	{'open_tab': {'url': BANK_URL_MAPPING[BANK]}},
]
async def main(task:str)->pd.DataFrame | None:
    agent_state = AgentState()
    browser = Browser(
	config=BrowserConfig(new_context_config=BrowserContextConfig()))
    agent = Agent(task=task, llm=agent_llm, controller=controller,injected_agent_state=agent_state,
                    browser=browser,
	                initial_actions=initial_actions,
                    planner_llm=planner_llm,
                    use_vision_for_planner=False, planner_interval=1,
        )
    history = await agent.run(max_steps=20)
    agent_state.history.history = []
    with open('agent_state.json', 'w',encoding="utf8") as f:
        serialized = agent_state.model_dump_json(exclude={'history'})
        f.write(serialized)
    result = history.final_result()
    if result:
        parsed: Snapshots = Snapshots.model_validate_json(result)
        df = pd.DataFrame([snapshot.model_dump() for snapshot in parsed.snapshots])
        return df


if __name__ == '__main__':
    task = f"""
Scroll down to find the calculator, don't scroll too much or you will miss it.
"""
#     task = f"""
# Goto {BANK_URL_MAPPING[BANK]}.
# Scroll down to find the calculator. 
# Fill in the following information:
# Input all the following combinations of loan amount and period then extract the flat rate and annualised percentage rate:
# Loan Amount: $50,000, $100,000, $200,000, $300,000, $500,000, $800,000, $1,000,000, $1,500,000
# Period: 12 months, 24 months, 36 months, 60 months
# """
    asyncio.run(main(task))
