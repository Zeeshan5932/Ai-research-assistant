# from langchain_openai import ChatOpenAI
# from langchain.agents import initialize_agent, AgentType
# from agent.tools import get_tools
# from agent.memory import get_memory
# from agent.prompts import SYSTEM_PROMPT

# def get_research_agent():
#     llm = ChatOpenAI(
#         temperature=0,
#         model="gpt-4o-mini"
#     )

#     agent = initialize_agent(
#         tools=get_tools(),
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         memory=get_memory(),
#         verbose=True,
#         handle_parsing_errors=True,   # ⭐ THIS FIX
#         system_message=SYSTEM_PROMPT
#     )

#     return agent


from langchain_openai import ChatOpenAI
from langchain.agents.react.agent import create_react_agent
from langchain.agents import AgentExecutor
from langchain.prompts import PromptTemplate
from agent.tools import get_tools
from agent.memory import get_memory
from dotenv import load_dotenv

load_dotenv()

def get_research_agent():
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )

    tools = get_tools()
    memory = get_memory()

    prompt = PromptTemplate.from_template(
        """You are an AI research assistant that can search academic papers, summarize them, and provide citations.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
    )

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
    )

    return executor

