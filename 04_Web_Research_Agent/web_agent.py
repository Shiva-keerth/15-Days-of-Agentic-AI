"""
Day 4: Web Research Agent
Concept: Integrating live web search (DuckDuckGo or Tavily) to allow the LLM to pull real-time data from the internet.
"""
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

def research_topic(topic: str):
    llm = ChatOpenAI(temperature=0)
    search_tool = DuckDuckGoSearchRun()
    
    agent = initialize_agent(
        [search_tool], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    
    return agent.run(f"Search the web for recent news about: {topic}")

if __name__ == "__main__":
    research_topic("Latest advancements in LangGraph 2026")
