from core.base_agent import ResearchAgent
import time
import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor

class ResearchAnalyst(ResearchAgent):
    def __init__(self):
        super().__init__("Analyst AI", "Research Analyst", 10)

    def analyze_data(self, hypothesis: dict) -> dict:
        print(f"{self.name}: Processing dataset for '{hypothesis['topic']}'...")
        time.sleep(2)
        input_file = "data/input/healthcare_data.csv"
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{self.name}: No data file found at {input_file}")
        
        data = pd.read_csv(input_file)
        avg_gain = data['efficiency_gain'].mean()
        avg_cost_reduction = data['cost_reduction'].mean()
        
        # Topic-specific adjustment (mock)
        topic = hypothesis['topic'].lower()
        if "cancer" in topic:
            data['efficiency_gain'] *= 1.1  # Simulate higher efficiency for cancer-related topics
            data['outcome_improvement'] *= 1.05
        elif "skin" in topic or "dermat" in topic:
            data['cost_reduction'] *= 1.2  # Simulate higher cost savings for skin-related topics
        
        # Recalculate averages after adjustment
        avg_gain = data['efficiency_gain'].mean()
        avg_cost_reduction = data['cost_reduction'].mean()
        
        # Decision Tree model for efficiency
        X = data[['training_hours']]
        y_eff = data['efficiency_gain']
        eff_model = DecisionTreeRegressor(max_depth=3)
        eff_model.fit(X, y_eff)
        eff_r_squared = eff_model.score(X, y_eff)
        eff_pred = eff_model.predict(pd.DataFrame([[14]], columns=['training_hours']))[0]
        
        # Decision Tree model for outcome
        y_out = data['outcome_improvement']
        out_model = DecisionTreeRegressor(max_depth=3)
        out_model.fit(X, y_out)
        out_r_squared = out_model.score(X, y_out)
        out_pred = out_model.predict(pd.DataFrame([[14]], columns=['training_hours']))[0]
        
        # Log model details
        with open("data/output/model_log.txt", "a") as f:
            f.write(f"{time.ctime()}: Efficiency DT - R²={eff_r_squared:.2f}, Outcome DT - R²={out_r_squared:.2f}\n")
        
        recommendation = "Increase training hours to 14+ for optimal efficiency and outcomes" if eff_pred > avg_gain else "Optimize current training process"
        
        return {
            "topic": hypothesis["topic"],
            "insights": (
                f"Analysis of {len(data)} records: avg efficiency {avg_gain:.1f}%, "
                f"avg cost reduction {avg_cost_reduction:.1f}%, "
                f"efficiency DT (R²={eff_r_squared:.2f}) predicts {eff_pred:.1f}% for 14 hours, "
                f"outcome DT (R²={out_r_squared:.2f}) predicts {out_pred:.1f}% improvement. "
                f"Recommendation: {recommendation}."
            )
        }