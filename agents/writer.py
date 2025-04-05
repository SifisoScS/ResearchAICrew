from core.base_agent import ResearchAgent
import time
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_report.md"
        try:
            with open(filename, 'w') as f:
                f.write(report)
            print(f"{self.name}: Markdown report saved to {filename}")
        except Exception as e:
            print(f"{self.name}: Failed to save report: {e}")
        
        white_paper = f"White Paper: {hypothesis['topic']} - Detailed analysis and future directions.\n\n{report}"
        white_paper_file = f"{output_dir}/{hypothesis['topic'].replace(' ', '_')}_white_paper.txt"
        try:
            with open(white_paper_file, "w") as f:
                f.write(white_paper)
            print(f"{self.name}: White paper saved to {white_paper_file}")
        except Exception as e:
            print(f"{self.name}: Failed to save white paper: {e}")
        
        self.create_visualization(hypothesis['topic'], analysis.get('nn_predictions', {}))
        return report

    def create_visualization(self, topic: str, nn_predictions: dict = None) -> None:
        print(f"{self.name}: Generating visualization for '{topic}'...")
        if "prostate cancer" in topic.lower():
            data = pd.DataFrame({
                'training_hours': [10, 12, 15, 11, 13],
                'efficiency_gain': [18, 20, 22, 19, 21],
                'outcome_improvement': [85, 88, 92, 87, 90],
                'cost_reduction': [5, 6, 8, 5.5, 7]
            })
        else:
            try:
                data = pd.read_csv("data/input/healthcare_data.csv")
            except FileNotFoundError:
                print(f"{self.name}: No fallback data found, using default mock data.")
                data = pd.DataFrame({
                    'training_hours': [10, 12, 15, 11, 13],
                    'efficiency_gain': [15, 17, 20, 16, 18],
                    'outcome_improvement': [80, 82, 85, 81, 83],
                    'cost_reduction': [4, 5, 6, 4.5, 5.5]
                })
        
        fig, ax1 = plt.subplots(figsize=(10, 6))
        ax1.scatter(data['training_hours'], data['efficiency_gain'], color='blue', label='Efficiency (%)')
        if nn_predictions and 'efficiency' in nn_predictions:
            ax1.plot(14, nn_predictions['efficiency'], 'b*', markersize=15, label=f'NN Eff Pred (14h): {nn_predictions["efficiency"]:.1f}%')
        ax1.set_xlabel('Training Hours')
        ax1.set_ylabel('Efficiency Gain (%)', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        
        ax2 = ax1.twinx()
        ax2.scatter(data['training_hours'], data['outcome_improvement'], color='green', label='Outcome (%)')
        if nn_predictions and 'outcome' in nn_predictions:
            ax2.plot(14, nn_predictions['outcome'], 'g*', markersize=15, label=f'NN Out Pred (14h): {nn_predictions["outcome"]:.1f}%')
        ax2.set_ylabel('Outcome Improvement (%)', color='green')
        ax2.tick_params(axis='y', labelcolor='green')
        
        ax3 = ax1.twinx()
        ax3.spines['right'].set_position(('outward', 60))
        ax3.scatter(data['training_hours'], data['cost_reduction'], color='red', label='Cost Reduction (%)')
        ax3.set_ylabel('Cost Reduction (%)', color='red')
        ax3.tick_params(axis='y', labelcolor='red')
        
        plt.title(f'Multi-Metric Analysis for {topic}')
        lines = [ax1.plot([], [], 'b-')[0], ax2.plot([], [], 'g-')[0], ax3.plot([], [], 'r-')[0]]
        labels = ['Efficiency', 'Outcome', 'Cost Reduction']
        if nn_predictions:
            lines.extend([ax1.plot([], [], 'b*')[0], ax2.plot([], [], 'g*')[0]])
            labels.extend([f'NN Eff Pred (14h)', f'NN Out Pred (14h)'])
        plt.legend(lines, labels, loc='upper left')
        plt.grid(True)
        
        # Ensure static directory exists
        static_dir = "static"
        os.makedirs(static_dir, exist_ok=True)
        
        plot_file = f"{static_dir}/{topic.replace(' ', '_')}_multi_metric_plot.png"
        try:
            plt.savefig(plot_file)
            plt.close()
            print(f"{self.name}: Plot saved to {plot_file}")
        except Exception as e:
            print(f"{self.name}: Failed to save plot: {e}")

    def draft_user_guide(self, topic: str) -> None:
        print(f"{self.name}: Drafting user guide for '{topic}'...")
        time.sleep(1)
        guide = f"User Guide: Implementing ML in {topic}\n1. Collect data\n2. Train model\n3. Evaluate results"
        guide_file = f"data/output/{topic.replace(' ', '_')}_guide.txt"
        try:
            with open(guide_file, "w") as f:
                f.write(guide)
            print(f"{self.name}: User guide saved to {guide_file}")
        except Exception as e:
            print(f"{self.name}: Failed to save user guide: {e}")

    def publish(self, topic: str) -> None:
        print(f"{self.name}: Publishing research for '{topic}'...")
        time.sleep(1)
        publish_log = "data/output/publish_log.txt"
        try:
            with open(publish_log, "a") as f:
                f.write(f"{time.ctime()}: Published {topic} to Tech AI Journal\n")
            print(f"{self.name}: Publication logged to {publish_log}")
        except Exception as e:
            print(f"{self.name}: Failed to log publication: {e}")