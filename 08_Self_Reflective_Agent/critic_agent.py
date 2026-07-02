"""
Day 8: Self-Reflective Agent
Concept: The agent generates an answer, critiques its own answer for hallucinations, and regenerates if needed.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def reflective_generation(query: str):
    generator_llm = ChatOpenAI(temperature=0.7)
    critic_llm = ChatOpenAI(temperature=0) # Zero temp for strict grading
    
    # Generate
    draft = generator_llm.invoke(f"Answer this: {query}").content
    
    # Critique
    critique_prompt = f"Review this answer: {draft}. Is it perfectly accurate? If yes, output OK. If no, output the correction."
    critique = critic_llm.invoke(critique_prompt).content
    
    return {"draft": draft, "critique": critique}

if __name__ == "__main__":
    print(reflective_generation("Explain quantum physics in one sentence."))
