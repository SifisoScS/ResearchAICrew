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
        output_dir = "data/output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_report.txt"
        with open(filename, 'w') as f:
            f.write(report)
        print(f"{self.name}: Report saved to {filename}")
        
        # White paper
        white_paper = f"White Paper: {hypothesis['topic']} - Detailed analysis and future directions.\n{report}"
        with open(f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_white_paper.txt", "w") as f:
            f.write(white_paper)
        print(f"{self.name}: White paper saved.")
        
        return report

    def draft_user_guide(self, topic: str) -> None:
        print(f"{self.name}: Drafting user guide for '{topic}'...")
        time.sleep(1)
        guide = f"User Guide: Implementing ML in {topic}\n1. Collect data\n2. Train model\n3. Evaluate results"
        with open(f"data/output/{topic.replace(' ', '_')}_guide.txt", "w") as f:
            f.write(guide)
        print(f"{self.name}: User guide saved.")

    def publish(self, topic: str) -> None:
        print(f"{self.name}: Publishing research for '{topic}'...")
        time.sleep(1)
        with open("data/output/publish_log.txt", "a") as f:
            f.write(f"{time.ctime()}: Published {topic} to Tech AI Journal\n")