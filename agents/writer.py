from core.base_agent import ResearchAgent
import time
import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
        
        # Create a subplot with three y-axes
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # Efficiency scatter
        fig.add_trace(
            go.Scatter(
                x=data['training_hours'],
                y=data['efficiency_gain'],
                mode='markers',
                name='Efficiency (%)',
                marker=dict(color='blue', size=10),
                hovertemplate='Training Hours: %{x}<br>Efficiency: %{y}%<extra></extra>'
            ),
            secondary_y=False
        )
        
        # NN Efficiency prediction
        if nn_predictions and 'efficiency' in nn_predictions:
            fig.add_trace(
                go.Scatter(
                    x=[14],
                    y=[nn_predictions['efficiency']],
                    mode='markers',
                    name=f'NN Eff Pred (14h): {nn_predictions["efficiency"]:.1f}%',
                    marker=dict(color='blue', symbol='star', size=15),
                    hovertemplate='Training Hours: 14<br>Efficiency: %{y}%<extra></extra>'
                ),
                secondary_y=False
            )
        
        # Outcome scatter
        fig.add_trace(
            go.Scatter(
                x=data['training_hours'],
                y=data['outcome_improvement'],
                mode='markers',
                name='Outcome (%)',
                marker=dict(color='green', size=10),
                hovertemplate='Training Hours: %{x}<br>Outcome: %{y}%<extra></extra>'
            ),
            secondary_y=True
        )
        
        # NN Outcome prediction
        if nn_predictions and 'outcome' in nn_predictions:
            fig.add_trace(
                go.Scatter(
                    x=[14],
                    y=[nn_predictions['outcome']],
                    mode='markers',
                    name=f'NN Out Pred (14h): {nn_predictions["outcome"]:.1f}%',
                    marker=dict(color='green', symbol='star', size=15),
                    hovertemplate='Training Hours: 14<br>Outcome: %{y}%<extra></extra>'
                ),
                secondary_y=True
            )
        
        # Cost Reduction scatter (on the same axis as Outcome for simplicity)
        fig.add_trace(
            go.Scatter(
                x=data['training_hours'],
                y=data['cost_reduction'],
                mode='markers',
                name='Cost Reduction (%)',
                marker=dict(color='red', size=10),
                hovertemplate='Training Hours: %{x}<br>Cost Reduction: %{y}%<extra></extra>',
                yaxis='y3'
            )
        )
        
        # Update layout
        fig.update_layout(
            title=f'Multi-Metric Analysis for {topic}',
            xaxis_title='Training Hours',
            yaxis_title='Efficiency Gain (%)',
            yaxis2_title='Outcome Improvement / Cost Reduction (%)',
            yaxis3=dict(
                title='Cost Reduction (%)',
                overlaying='y2',
                side='right',
                showgrid=False
            ),
            legend=dict(x=0, y=1.1, orientation='h'),
            hovermode='closest',
            plot_bgcolor='white',
            margin=dict(t=100)
        )
        
        # Update axes (fixed titlefont to title_font)
        fig.update_yaxes(title_font=dict(color='blue'), tickfont=dict(color='blue'), secondary_y=False)
        fig.update_yaxes(title_font=dict(color='green'), tickfont=dict(color='green'), secondary_y=True)
        
        # Save as HTML
        plot_file = f"static/{topic.replace(' ', '_')}_multi_metric_plot.html"
        try:
            fig.write_html(plot_file)
            print(f"{self.name}: Interactive plot saved to {plot_file}")
        except Exception as e:
            print(f"{self.name}: Failed to save interactive plot: {e}")

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