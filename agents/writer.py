from core.base_agent import ResearchAgent
import time

class ResearchTechnicalWriter(ResearchAgent):
    def __init__(self):
        super().__init__("Writer AI", "Research Technical Writer", 10)

    def write_report(self, hypothesis: dict, analysis: dict) -> str:
        print(f"{self.name}: Writing report for '{hypothesis['topic']}'...")
        time.sleep(1.5)
        return (
            f"Research Report: {hypothesis['topic']}\n"
            f"Hypothesis: {hypothesis['hypothesis']}\n"
            f"Findings: {analysis['insights']}\n"
            f"Conclusion: Promising results warrant further study."
        ) 
