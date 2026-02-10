from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from agent.tools import get_tools
from dotenv import load_dotenv

load_dotenv()

# Import from langgraph.prebuilt (modern LangChain 0.2+)
try:
    from langgraph.prebuilt import create_react_agent  # type: ignore
    _USE_LANGGRAPH = True
except ImportError:
    _USE_LANGGRAPH = False
    create_react_agent = None


def get_research_agent():
    """Create and return a research agent using ReAct pattern."""
    
    # Use ChatOpenAI (or swap to another LLM as needed)
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    
    # Uncomment below to use Google Generative AI instead
    # llm = ChatGoogleGenerativeAI(
    #     model="gemini-1.5-flash",
    #     temperature=0
    # )

    tools = get_tools()
    
    if not _USE_LANGGRAPH or create_react_agent is None:
        raise ImportError(
            "langgraph.prebuilt.create_react_agent not found. "
            "Please install a compatible version: pip install --upgrade langgraph langchain"
        )
    
    # Create agent using modern langgraph API
    agent_executor = create_react_agent(
        model=llm,
        tools=tools,
        debug=True  # Enable debug output
    )
    
    return agent_executor

