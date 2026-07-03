"""
Day 9: LangGraph Basics
Concept: Using LangGraph to build a state machine. Instead of linear chains, we define nodes (functions) and edges (control flow).
"""
from typing import TypedDict
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    input: str
    output: str

def node_a(state: AgentState):
    return {"output": state["input"] + " -> Processed by A"}

def node_b(state: AgentState):
    return {"output": state["output"] + " -> Processed by B"}

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("A", node_a)
    workflow.add_node("B", node_b)
    
    workflow.set_entry_point("A")
    workflow.add_edge("A", "B")
    workflow.add_edge("B", END)
    
    app = workflow.compile()
    return app

if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({"input": "Start"})
    print(result)
