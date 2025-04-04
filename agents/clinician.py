from core.base_agent import ResearchAgent
import time

class ClinicianAgent(ResearchAgent):
    def __init__(self):
        super().__init__("Dr. AI", "Clinical Advisor", 15)

    def provide_recommendations(self, hypothesis: dict, analysis: dict) -> str:
        print(f"{self.name}: Analyzing insights for clinical recommendations...")
        time.sleep(1)
        insights = analysis['insights']
        if "Increase training hours" in insights:
            return "Recommendation: Increase MRI-guided therapy training to 14+ hours to optimize prostate cancer detection efficiency."
        return "Recommendation: Optimize current protocols with AI-driven diagnostics."