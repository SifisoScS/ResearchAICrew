from core.base_agent import ResearchAgent
import time
import random

class ResearchAnalyst(ResearchAgent):
    def __init__(self):
        super().__init__("Analyst AI", "Research Analyst", 10)

    def analyze_data(self, hypothesis: dict) -> dict:
        print(f"{self.name}: Analyzing data for '{hypothesis['topic']}'...")
        time.sleep(2)
        return {
            "topic": hypothesis["topic"],
            "insights": f"Initial tests show {random.randint(15, 25)}% efficiency gain."
        } 
