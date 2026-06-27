"""
Day 1: Basic ReAct Agent
Concept: Reason + Act (ReAct) allows an LLM to think about what to do, choose a tool, observe the result, and then answer.
"""
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

def run_react_agent(query: str):
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    tools = load_tools(["llm-math"], llm=llm) # Basic math tool
    
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    return agent.run(query)

if __name__ == "__main__":
    print(run_react_agent("What is 25 divided by 5, multiplied by 10?"))
