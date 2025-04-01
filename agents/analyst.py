from core.base_agent import ResearchAgent
import time
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

class ResearchAnalyst(ResearchAgent):
    def __init__(self):
        super().__init__("Analyst AI", "Research Analyst", 10)

    def analyze_data(self, hypothesis: dict) -> dict:
        print(f"{self.name}: Analyzing data for '{hypothesis['topic']}'...")
        time.sleep(2)
        
        # Load data from CSV
        input_file = "data/input/healthcare_data.csv"
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{self.name}: No data file found at {input_file}")
        
        data = pd.read_csv(input_file)
        avg_gain = data['efficiency_gain'].mean()
        
        # Train simple linear regression model (efficiency_gain vs training_hours)
        X = data[['training_hours']]  # Feature
        y = data['efficiency_gain']   # Target
        model = LinearRegression()
        model.fit(X, y)
        r_squared = model.score(X, y)
        
        # Predict efficiency for 14 training hours
        predicted_gain = model.predict([[14]])[0]
        
        return {
            "topic": hypothesis["topic"],
            "insights": (
                f"Analysis of {len(data)} records shows average {avg_gain:.1f}% efficiency gain. "
                f"Linear model (R²={r_squared:.2f}) predicts {predicted_gain:.1f}% gain for 14 training hours."
            )
        }