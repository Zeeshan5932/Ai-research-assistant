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
from agent.tools import get_tools
from agent.memory import get_memory
from agent.prompts import SYSTEM_PROMPT


try:
    from langchain.agents import create_agent
except Exception:
    create_agent = None


class _DummyAgent:
    def invoke(self, *args, **kwargs):
        raise RuntimeError(
            "LangChain agent creation API not available.\n"
            "Install a compatible LangChain version or update the code. "
            "E.g., try `pip install 'langchain>=0.1.0,<0.1.100'` or adjust imports.`"
        )


def get_research_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    tools = get_tools()

    if create_agent is not None:
        agent = create_agent(llm=llm, tools=tools, memory=get_memory())
        return agent

    return _DummyAgent()
