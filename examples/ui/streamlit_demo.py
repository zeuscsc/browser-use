"""
To use it, you'll need to install streamlit, and run with:

python -m streamlit run streamlit_demo.py

"""

import os
import sys
import asyncio
import streamlit as st
from dotenv import load_dotenv

# Ensure local repository (browser_use) is accessible
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller

# Load environment variables
load_dotenv()

# Function to get the LLM based on provider
def get_llm(provider: str):
    if provider == 'anthropic':
        from langchain_anthropic import ChatAnthropic
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            st.error("Error: ANTHROPIC_API_KEY is not set. Please provide a valid API key.")
            st.stop()
        
        return ChatAnthropic(
            model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0
        )
    elif provider == 'openai':
        from langchain_openai import ChatOpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("Error: OPENAI_API_KEY is not set. Please provide a valid API key.")
            st.stop()
        
        return ChatOpenAI(model='gpt-4o', temperature=0.0)
    else:
        st.error(f'Unsupported provider: {provider}')
        st.stop()

# Function to initialize the agent
def initialize_agent(query: str, provider: str):
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

# Streamlit UI
st.title("Automated Browser Agent with LLMs 🤖")

query = st.text_input("Enter your query:", "go to reddit and search for posts about browser-use")
provider = st.radio("Select LLM Provider:", ["openai", "anthropic"], index=0)

if st.button("Run Agent"):
    st.write("Initializing agent...")
    agent, browser = initialize_agent(query, provider)

    async def run_agent():
        with st.spinner("Running automation..."):
            await agent.run(max_steps=25)
        st.success("Task completed! 🎉")

    asyncio.run(run_agent())

    st.button("Close Browser", on_click=lambda: asyncio.run(browser.close()))
