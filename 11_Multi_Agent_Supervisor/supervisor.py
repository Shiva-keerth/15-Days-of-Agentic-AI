"""
Day 11: Multi-Agent Supervisor
Concept: A hierarchical system where a 'Supervisor' LLM receives a task and delegates it to specialist workers (e.g., Coder, Researcher).
"""
from langchain_core.prompts import ChatPromptTemplate

system_prompt = (
    "You are a supervisor managing a conversation between these workers: "
    "[Researcher, Coder]. Given a user request, respond with the worker to act next. "
    "If the task is finished, respond with FINISH."
)

print("Supervisor agent prompt templates and routing logic configured.")
