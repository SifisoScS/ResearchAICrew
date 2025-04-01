from core.base_agent import ResearchAgent
import time
import os

class ResearchTechnicalWriter(ResearchAgent):
    def __init__(self):
        super().__init__("Writer AI", "Research Technical Writer", 10)

    def write_report(self, hypothesis: dict, analysis: dict) -> str:
        print(f"{self.name}: Writing report for '{hypothesis['topic']}'...")
        time.sleep(1.5)
        report = (
            f"Research Report: {hypothesis['topic']}\n"
            f"Hypothesis: {hypothesis['hypothesis']}\n"
            f"Findings: {analysis['insights']}\n"
            f"Conclusion: Promising results warrant further study."
        )
        # Save to file
        output_dir = "data/output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_report.txt"
        with open(filename, 'w') as f:
            f.write(report)
        print(f"{self.name}: Report saved to {filename}")
        return report