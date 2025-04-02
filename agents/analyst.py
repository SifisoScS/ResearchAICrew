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
        
        # Train and test ML model
        X = data[['training_hours']]
        y = data['efficiency_gain']
        model = LinearRegression()
        model.fit(X, y)
        r_squared = model.score(X, y)
        predicted_gain = model.predict([[14]])[0]
        
        # Log model details
        with open("data/output/model_log.txt", "a") as f:
            f.write(f"{time.ctime()}: Model for {hypothesis['topic']} - R²={r_squared:.2f}, Slope={model.coef_[0]:.2f}\n")
        
        # Actionable insight
        recommendation = "Increase training hours to 14+ for optimal efficiency" if predicted_gain > avg_gain else "Optimize current training process"
        
        return {
            "topic": hypothesis["topic"],
            "insights": (
                f"Analysis of {len(data)} records shows average {avg_gain:.1f}% efficiency gain. "
                f"Linear model (R²={r_squared:.2f}) predicts {predicted_gain:.1f}% gain for 14 hours. "
                f"Recommendation: {recommendation}."
            )
        }