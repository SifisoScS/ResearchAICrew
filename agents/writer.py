from core.base_agent import ResearchAgent
import time
import os
import matplotlib.pyplot as plt

class ResearchTechnicalWriter(ResearchAgent):
    def __init__(self):
        super().__init__("Writer AI", "Research Technical Writer", 10)

    def write_report(self, hypothesis: dict, analysis: dict) -> str:
        print(f"{self.name}: Writing report for '{hypothesis['topic']}'...")
        time.sleep(1.5)
        report = (
            f"# Research Report: {hypothesis['topic']}\n\n"
            f"## Hypothesis\n{hypothesis['hypothesis']}\n\n"
            f"## Findings\n{analysis['insights']}\n\n"
            f"## Conclusion\nPromising results warrant further study."
        )
        output_dir = "data/output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_report.md"
        with open(filename, 'w') as f:
            f.write(report)
        print(f"{self.name}: Markdown report saved to {filename}")
        
        # White paper
        white_paper = f"White Paper: {hypothesis['topic']} - Detailed analysis and future directions.\n\n{report}"
        with open(f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_white_paper.txt", "w") as f:
            f.write(white_paper)
        print(f"{self.name}: White paper saved.")
        
        # Visualization
        self.create_visualization(hypothesis['topic'])
        
        return report

    def create_visualization(self, topic: str) -> None:
        print(f"{self.name}: Generating visualization for '{topic}'...")
        import pandas as pd
        data = pd.read_csv("data/input/healthcare_data.csv")
        plt.figure(figsize=(8, 6))
        plt.scatter(data['training_hours'], data['efficiency_gain'], color='blue', label='Data')
        plt.xlabel('Training Hours')
        plt.ylabel('Efficiency Gain (%)')
        plt.title(f'Efficiency Gain vs Training Hours in {topic}')
        plt.legend()
        plt.grid(True)
        plot_file = f"data/output/{topic.replace(' ', '_')}_efficiency_plot.png"
        plt.savefig(plot_file)
        plt.close()
        print(f"{self.name}: Plot saved to {plot_file}")

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