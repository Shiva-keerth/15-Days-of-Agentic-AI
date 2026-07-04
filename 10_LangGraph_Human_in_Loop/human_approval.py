"""
Day 10: LangGraph Human-in-the-Loop
Concept: Pausing the graph execution to ask a human for approval before taking a destructive action (like dropping a database).
"""
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    action: str
    approved: bool

def determine_action(state: State):
    return {"action": "Delete Production Database"}

def execute_action(state: State):
    if state.get("approved"):
        return {"action": state["action"] + " [EXECUTED]"}
    return {"action": state["action"] + " [DENIED]"}

def should_execute(state: State):
    return "execute" if state.get("approved") else END

# Note: In a real app, we use checkpointer interrupts for this.
print("Human-in-the-loop architecture initialized. Waiting for approval interrupt.")
