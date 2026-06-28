"""
Day 3: Custom Tool Calling Agent
Concept: Building our own custom Python functions and giving them to the LLM so it can execute code on our behalf.
"""
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

@tool
def get_user_status(user_id: int) -> str:
    """Returns the subscription status of a user given their ID."""
    db = {1: "Premium", 2: "Free", 3: "Banned"}
    return db.get(user_id, "User not found")

def run_custom_tool_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [get_user_status]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful customer support agent."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    agent_executor.invoke({"input": "What is the status of user ID 1?"})

if __name__ == "__main__":
    run_custom_tool_agent()
