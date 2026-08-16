from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from config import GOOGLE_MODEL

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


class ResearchAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=GOOGLE_MODEL,
            temperature=0,
        )

    def run(self, input: str):
        messages = [
            SystemMessage(
                content=(
                    "You are an AI research assistant. "
                    "Answer clearly, summarize research papers well, and include citations "
                    "when discussing paper content."
                )
            ),
            HumanMessage(content=input),
        ]

        response = self.llm.invoke(messages)
        return getattr(response, "content", str(response))


def get_research_agent():
    return ResearchAgent()