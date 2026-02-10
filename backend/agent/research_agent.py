from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import get_tools
from agent.memory import get_memory
from agent.prompts import SYSTEM_PROMPT

def get_research_agent():
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )

    agent = initialize_agent(
        tools=get_tools(),
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=get_memory(),
        verbose=True,
        handle_parsing_errors=True,   # ⭐ THIS FIX
        system_message=SYSTEM_PROMPT
    )

    return agent
