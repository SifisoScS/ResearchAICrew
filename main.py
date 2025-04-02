# main.py should be:
from workflows.research_flow import research_workflow

if __name__ == "__main__":
    topic = input("Enter research topic (e.g., Machine Learning in Healthcare): ") or "Machine Learning in Healthcare"
    print(f"Starting research on: {topic}\n")
    research_workflow(topic)