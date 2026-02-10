# from langchain_openai import ChatOpenAI
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain.prompts import (
#     ChatPromptTemplate,
#     MessagesPlaceholder,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )
# from agent.tools import get_tools
# from agent.memory import get_memory
# from dotenv import load_dotenv
# load_dotenv()

# def get_research_agent():
#     llm = ChatOpenAI(
#         model="gpt-4o-mini",
#         temperature=0
#     )

#     tools = get_tools()
#     memory = get_memory()

#     # ✅ ReAct-style prompt (STABLE) - use message templates so placeholders have correct types
#     prompt = ChatPromptTemplate.from_messages([
#         SystemMessagePromptTemplate.from_template(
#             "You are an AI research assistant. "
#             "You search academic papers, summarize them, and cite sources. "
#             "You have access to the following tools: {tools} \nTool names: {tool_names}"
#         ),
#         MessagesPlaceholder(variable_name="chat_history"),
#         HumanMessagePromptTemplate.from_template("{input}"),
#         MessagesPlaceholder(variable_name="agent_scratchpad"),
#     ])

#     agent = create_react_agent(
#         llm=llm,
#         tools=tools,
#         prompt=prompt
#     )

#     executor = AgentExecutor(
#         agent=agent,
#         tools=tools,
#         memory=memory,
#         verbose=True,
#         handle_parsing_errors=True
#     )

#     return executor


from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from agent.tools import get_tools
# from agent.memory import get_memory
from dotenv import load_dotenv
import importlib

load_dotenv()

# Try to import modern LangChain agent API, otherwise fall back to older helpers
_HAS_INITIALIZE = False
try:
    from langchain.agents import initialize_agent, AgentType  # type: ignore
    _HAS_INITIALIZE = True
except Exception:
    try:
        from langchain.agents import create_react_agent, AgentExecutor  # type: ignore
    except Exception:
        create_react_agent = None
        AgentExecutor = None


def get_research_agent():
    # Default to ChatOpenAI; swap to another LLM if you have one configured
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    
    # llm = ChatGoogleGenerativeAI(
    #     model="gemini-1.5-flash",
    #     temperature=0
    # )

    tools = get_tools()
    # memory = get_memory()

    prompt = PromptTemplate.from_template("""You are an AI research assistant.
You search academic papers, summarize them, compare them, and cite sources.

You have access to the following tools:
{tools}

Tool names: {tool_names}

Question: {input}
{agent_scratchpad}""")

    if _HAS_INITIALIZE:
        executor = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        
            verbose=True,
            handle_parsing_errors=True,
        )
        return executor

    # Fallback for older LangChain versions
    if create_react_agent is None or AgentExecutor is None:
        raise ImportError(
            "No supported agent API found in installed langchain package. "
            "Install a LangChain version that provides `initialize_agent` or `create_react_agent`."
        )

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        
        verbose=True,
        handle_parsing_errors=True
    )

    return executor

