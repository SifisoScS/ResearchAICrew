from core.base_agent import ResearchAgent
import time
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

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
        
        # Efficiency model
        X_eff = data[['training_hours']]
        y_eff = data['efficiency_gain']
        eff_model = LinearRegression()
        eff_model.fit(X_eff, y_eff)
        eff_r_squared = eff_model.score(X_eff, y_eff)
        eff_pred = eff_model.predict(pd.DataFrame([[14]], columns=['training_hours']))[0]
        
        # Outcome model
        X_out = data[['training_hours']]
        y_out = data['outcome_improvement']
        out_model = LinearRegression()
        out_model.fit(X_out, y_out)
        out_r_squared = out_model.score(X_out, y_out)
        out_pred = out_model.predict(pd.DataFrame([[14]], columns=['training_hours']))[0]
        
        # Log model details
        with open("data/output/model_log.txt", "a") as f:
            f.write(f"{time.ctime()}: Efficiency Model - R²={eff_r_squared:.2f}, Outcome Model - R²={out_r_squared:.2f}\n")
        
        recommendation = "Increase training hours to 14+ for optimal efficiency and outcomes" if eff_pred > avg_gain else "Optimize current training process"
        
        return {
            "topic": hypothesis["topic"],
            "insights": (
                f"Analysis of {len(data)} records: avg efficiency {avg_gain:.1f}%, "
                f"efficiency model (R²={eff_r_squared:.2f}) predicts {eff_pred:.1f}% for 14 hours, "
                f"outcome model (R²={out_r_squared:.2f}) predicts {out_pred:.1f}% improvement. "
                f"Recommendation: {recommendation}."
            )
        }