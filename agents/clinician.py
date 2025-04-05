from core.base_agent import ResearchAgent
import time

class ClinicianAgent(ResearchAgent):
    def __init__(self):
        super().__init__("Dr. AI", "Clinical Advisor", 15)

    def provide_recommendations(self, hypothesis: dict, analysis: dict) -> str:
        print(f"{self.name}: Analyzing insights for clinical recommendations...")
        time.sleep(1)
        insights = analysis['insights']
        topic = hypothesis['topic'].lower()
        if "prostate cancer" in topic:
            if "Increase training hours" in insights:
                return (
                    "Clinical Recommendation: Increase MRI-guided therapy training to 14+ hours to optimize prostate cancer detection efficiency. "
                    "This may improve early diagnosis rates and patient outcomes."
                )
            else:
                return (
                    "Clinical Recommendation: Optimize current protocols with AI-driven diagnostics for prostate cancer. "
                    "Focus on integrating ML models into PSA screening workflows to enhance accuracy."
                )
        return "Clinical Recommendation: Further research needed to provide specific guidance."