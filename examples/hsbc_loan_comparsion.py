import asyncio
import os
from typing import Any, Coroutine
import re
import pandas as pd

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent, AgentHistoryList
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
api_key = os.getenv('OPEN_ROUTER_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

# llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    # model='deepseek/deepseek-r1-distill-llama-70b',
    model="deepseek/deepseek-r1",
    # model="openai/o1-mini",
    api_key=SecretStr(api_key),
    )
# result=llm.invoke(input="Hello, world!")
# print(result)
# exit()

def save_history_pipeline(history:AgentHistoryList,project_name,agent_name):
    history.save_to_file(os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".json"))
    if os.path.exists(os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".gif")):
        os.remove(os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".gif"))
    os.rename("agent_history.gif",os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".gif"))
    return
def extract_answer_from_tag(tag:str,text:str)->str|None:
    pattern="<"+tag+">(.+?)</"+tag+">"
    result=re.search(pattern,text)
    if result is not None:
        return result.group(1)
    else:
        return None
async def main():
    df=pd.DataFrame(columns=["bank","loan_amount","period","flat_rate","apr"])
    config=BrowserConfig(
        headless=False,  # This is True in production
        disable_security=True,
        )
    new_context_config=BrowserContextConfig(
            disable_security=True,
            minimum_wait_page_load_time=1,  # 3 on prod
            maximum_wait_page_load_time=10,  # 20 on prod
            # no_viewport=True,
            # browser_window_size={
            # 	'width': 2560,
            # 	'height': 1600,
            # },
            # trace_path='./tmp/web_voyager_agent',
        )
    browser = Browser(config=config)
    async with await browser.new_context(config=new_context_config) as context:
        model = llm
        bank="HASE"
        loan_amount = 50000
        period=12
        bank_list=["HASE"]
        bank_url_mapping={
             "HASE":"https://www.hangseng.com/en-hk/personal/loans/instalment-loan/",
             "BoC":"https://www.bochk.com/dam/loans/personal/instalmentloan/tc.html"
            }
        loan_amount_list=[50000,1000000,2000000,3000000,5000000,800000,10000000,1500000]
        period_list=[12,24,36,60]
        loan_amount_list=[loan_amount]
        period_list=[period]
        for bank in bank_list:
            for loan_amount in loan_amount_list:
                for period in period_list:
                    async def run_agent_pipeline()->AgentHistoryList:
                        url=bank_url_mapping[bank]
                        setting_task="""Go to {url}
Scroll down to find the Loan Calculator if needed (Half page each scroll).
Empty the Loan Amount input.
Empty the Loan Period input.
Replace Loan Amount input to {loan_amount} (Make sure the value is the same).
Replace Loan Period input to {period} (Make sure the value is the same).
"""
                        setting_task=setting_task.format(url=url,loan_amount=loan_amount,period=period)
                        agent_rate_settings = Agent(
                            task=setting_task,
                            llm=model,
                            browser_context=context,
                            tool_call_in_content=True,
                            use_vision=False,
                        )
                        agent_rate_extract = Agent(
                            task="""Extract the flat rate and the Annualised Percentage Rate (”APR“) for me.
Wrap the extracted information to me in a tag.
Example:
<flat_rate>1.5%</flat_rate>
<APR>3.5%</APR>""",
                            llm=model,
                            browser_context=context,
                            tool_call_in_content=True,
                            use_vision=False,
                        )
                        history=await agent_rate_settings.run(max_steps=10);save_history_pipeline(history,"hsbc_loan_comparsion",f"agent_rate_settings_{bank}_{loan_amount}_{period}")
                        history=await agent_rate_extract.run(max_steps=10);save_history_pipeline(history,"hsbc_loan_comparsion",f"agent_rate_extract_{bank}_{loan_amount}_{period}")
                        return history
                    last_history=(await run_agent_pipeline()).last_action()
                    if last_history is not None:
                        extracted_text=last_history["done"]["text"]
                        flat_rate=extract_answer_from_tag("flat_rate",extracted_text)
                        apr=extract_answer_from_tag("APR",extracted_text)
                        df = pd.concat([df, 
                                        pd.DataFrame([{
                                            "bank": bank,
                                            "loan_amount": loan_amount,
                                            "period": period,
                                            "flat_rate": flat_rate,
                                            "apr": apr
                                         }])], ignore_index=True)
        os.makedirs(os.path.join(os.path.dirname(__file__),"results"),exist_ok=True)    
        df.to_csv(os.path.join(os.path.dirname(__file__),"results","hsbc_loan_comparsion.csv"),index=False)
        await browser.close()


if __name__ == '__main__':
	asyncio.run(main())
