from core.base_agent import ResearchAgent
import time

class ResearchProfessor(ResearchAgent):
    def __init__(self):
        super().__init__("Prof. AI", "Research Professor", 7)

    def develop_hypothesis(self, topic: str) -> dict:
        print(f"{self.name}: Formulating hypothesis for '{topic}'...")
        time.sleep(1)
        return {
            "topic": topic,
            "hypothesis": f"Can {topic} improve efficiency by 20% using advanced ML techniques?",
            "research_plan": ["Literature review", "Identify gaps", "Propose ML model"]
        } 
