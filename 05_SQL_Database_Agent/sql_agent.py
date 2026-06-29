"""
Day 5: SQL Database Agent
Concept: Text-to-SQL. The agent looks at the database schema and writes SQL queries to answer natural language questions.
"""
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# Note: Requires a local sqlite file to run
def query_database(question: str, db_path: str = "sqlite:///sample.db"):
    llm = ChatOpenAI(temperature=0)
    try:
        db = SQLDatabase.from_uri(db_path)
        agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
        agent_executor.invoke({"input": question})
    except Exception as e:
        print("Database not found, please create sample.db first.")

if __name__ == "__main__":
    query_database("How many users signed up last month?")
