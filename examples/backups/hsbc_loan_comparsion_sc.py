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
import json

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext


load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
open_router_api_key = os.getenv('OPEN_ROUTER_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')
if not open_router_api_key:
    raise ValueError('OPEN_ROUTER_API_KEY is not set')

# llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
llm = ChatGoogleGenerativeAI(model='gemini-2.0-pro-exp-02-05', api_key=SecretStr(api_key))
rl_llm = ChatOpenAI(
			base_url='https://openrouter.ai/api/v1',
            model="qwen/qwq-32b",
            api_key=SecretStr(open_router_api_key))

PROJECT_NAME="hsbc_loan_comparsion_sc"
df_path=os.path.join(os.path.dirname(__file__),"results",f"{PROJECT_NAME}.csv")
df=pd.DataFrame(columns=["bank","loan_amount","period","flat_rate","apr"])
bank="SC"
loan_amount = 50000
period=12
bank_list=["SC"]
bank_url_mapping={
        "HASE":"https://www.hangseng.com/en-hk/personal/loans/instalment-loan/",
        "BoC":"https://www.bochk.com/dam/loans/personal/instalmentloan/tc.html",
        "SC":"https://www.sc.com/hk/loans/personal-instalment-loan/"
    }
loan_amount_list=[50000,1000000,2000000,3000000,5000000,800000,10000000,1500000]
# loan_amount_list=[50000,1000000,2000000,3000000]
period_list=[12]

def save_history_pipeline(history:AgentHistoryList,project_name,agent_name):
    history.save_to_file(os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".json"))
    if os.path.exists(os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".gif")):
        os.remove(os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".gif"))
    try:
        os.rename("agent_history.gif",os.path.join(os.path.dirname(__file__),"tmp",project_name,agent_name+".gif"))
    except:
        pass
    return
def extract_answer_from_tag(tag:str,text:str)->str|None:
    pattern="<"+tag+">(.+?)</"+tag+">"
    result=re.search(pattern,text)
    if result is not None:
        return result.group(1)
    else:
        return None
async def perform_task(bank, loan_amount, period, url, df):
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
        async def run_agent_pipeline(url,bank,loan_amount,period):
            agent_rate_settings = Agent(
                task=f"""Go to {url}
Scroll down to find the SC Personal Instalment Loan Repayment Table (Half page each scroll).
The top is a calculator which is not the target, the target is the table below the calculator.
""",
                llm=llm,
                browser_context=context,
                # tool_call_in_content=False,
                # use_vision=False,
            )
            agent_rate_double_check = Agent(
                task=f"""Double check the Loan Amount and Loan Period for me.
Compare the Loan Amount drop down box to see if the range amount is {loan_amount}, if not, correct it.
Select the range that {loan_amount} should belong to.
Tell me if {loan_amount} can fit into the selected range or not.
Output True if it is are correct, False if not.
Wrap the output in a tag.
Example:
<correct>True</correct>
""",
                llm=llm,
                browser_context=context,
                # tool_call_in_content=False,
                # use_vision=False,
            )
            agent_rate_extract = Agent(
                task="""Extract the Loan Tenor paire up with flat rate and the Annualised Percentage Rate (”APR“) for me.
Put the extracted information into JSON and
Wrap the JSON in with a tag.
Example:
<json>[{"period":12,"flat_rate":0.1,"apr":0.2},{"period":24,"flat_rate":0.2,"apr":0.3}]</json>'
""",
                llm=llm,
                browser_context=context,
                # tool_call_in_content=False,
                # use_vision=False,
            )
            history=await agent_rate_settings.run(max_steps=20);save_history_pipeline(history,f"{PROJECT_NAME}",f"agent_rate_settings_{bank}_{loan_amount}_{period}")
            history=await agent_rate_double_check.run(max_steps=10);save_history_pipeline(history,f"{PROJECT_NAME}",f"agent_rate_double_check_{bank}_{loan_amount}_{period}")
            last_history=history.last_action()
            if last_history is not None and "done" in last_history:
                extracted_text=last_history["done"]["text"]
                correct = extract_answer_from_tag("correct", extracted_text)
                correct = (correct.lower() == "true") if correct is not None else False
                if not correct:
                    return None
            history=await agent_rate_extract.run(max_steps=5);save_history_pipeline(history,f"{PROJECT_NAME}",f"agent_rate_extract_{bank}_{loan_amount}_{period}")
            return history
        pipeline_result = await run_agent_pipeline(url=url, bank=bank, loan_amount=loan_amount, period=period)
        if pipeline_result is not None:
            last_history = pipeline_result.last_action()
        else:
            last_history = None
        if last_history is not None and "done" in last_history:
            extracted_text=last_history["done"]["text"]
            json_text = extract_answer_from_tag("json", extracted_text)
            print("json_text",json_text)
            if json_text is not None:
                rows = json.loads(json_text)
            else:
                rows = None
            if os.path.exists(os.path.join(os.path.dirname(__file__),"results",f"{PROJECT_NAME}.csv")):
                df=pd.read_csv(os.path.join(os.path.dirname(__file__),"results",f"{PROJECT_NAME}.csv"))
            if rows is not None:
                for row in rows:
                    df = pd.concat([df, 
                            pd.DataFrame([{
                                "bank": bank,
                                "loan_amount": loan_amount,
                                "period": row["period"],
                                "flat_rate": row["flat_rate"],
                                "apr": row["apr"]
                                }])], ignore_index=True)
        await browser.close()
        os.makedirs(os.path.join(os.path.dirname(__file__),"results"),exist_ok=True)    
        df.to_csv(os.path.join(os.path.dirname(__file__),"results",f"{PROJECT_NAME}.csv"),index=False)
async def batch_execute(tasks, batch_size):
    for i in tqdm(range(0, len(tasks), batch_size)):
        batch = tasks[i:i+batch_size]
        await asyncio.gather(*batch)
async def main(df:pd.DataFrame):
    tasks = []
    if os.path.exists(os.path.join(os.path.dirname(__file__),"results",f"{PROJECT_NAME}.csv")):
        df=pd.read_csv(os.path.join(os.path.dirname(__file__),"results",f"{PROJECT_NAME}.csv"))
    df = df.dropna(subset=['bank', 'loan_amount', 'period'])
    for bank in bank_list:
        url = bank_url_mapping[bank]
        for loan_amount in loan_amount_list:
            for period in period_list:
                if not df[(df['bank'] == bank) & 
                      (df['loan_amount'] == loan_amount) & 
                      (df['period'] == period)].empty:
                    continue
                print(f"Adding task for {bank} with loan amount {loan_amount} and period {period}")
                tasks.append(perform_task(bank, loan_amount, period, url,df))
    batch_size = 1  # Adjust based on your needs
    await batch_execute(tasks, batch_size)


if __name__ == '__main__':
    asyncio.run(main(df))
