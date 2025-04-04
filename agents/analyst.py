from core.base_agent import ResearchAgent
import time
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.preprocessing import StandardScaler

class ResearchAnalyst(ResearchAgent):
    def __init__(self):
        super().__init__("Analyst AI", "Research Analyst", 10)  # Name, role, experience level

    def fetch_prostate_cancer_data(self, topic: str) -> pd.DataFrame:
        print(f"{self.name}: Fetching topic-specific data for '{topic}'...")
        if "prostate cancer" in topic.lower():
            return pd.DataFrame({
                'training_hours': [10, 12, 15, 11, 13],
                'efficiency_gain': [18, 20, 22, 19, 21],
                'outcome_improvement': [85, 88, 92, 87, 90],
                'cost_reduction': [5, 6, 8, 5.5, 7],
                'survival_rate': [90, 92, 95, 91, 93]
            })
        try:
            return pd.read_csv("data/input/healthcare_data.csv")
        except FileNotFoundError:
            print(f"{self.name}: No fallback data found, using default mock data.")
            return pd.DataFrame({
                'training_hours': [10, 12, 15, 11, 13],
                'efficiency_gain': [15, 17, 20, 16, 18],
                'outcome_improvement': [80, 82, 85, 81, 83],
                'cost_reduction': [4, 5, 6, 4.5, 5.5]
            })

    def analyze_data(self, hypothesis: dict) -> dict:
        print(f"{self.name}: Processing dataset for '{hypothesis['topic']}'...")
        time.sleep(2)
        data = self.fetch_prostate_cancer_data(hypothesis['topic'])
        
        # Prepare data
        X = data[['training_hours']].values
        y_eff = data['efficiency_gain'].values
        y_out = data['outcome_improvement'].values
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Neural network for efficiency
        eff_model = Sequential([
            Input(shape=(1,)),
            Dense(16, activation='relu'),
            Dense(8, activation='relu'),
            Dense(1)
        ])
        eff_model.compile(optimizer='adam', loss='mse')
        eff_model.fit(X_scaled, y_eff, epochs=200, batch_size=2, verbose=0)
        eff_pred = float(eff_model.predict(scaler.transform([[14]]), verbose=0)[0][0])
        
        # Neural network for outcome
        out_model = Sequential([
            Input(shape=(1,)),
            Dense(16, activation='relu'),
            Dense(8, activation='relu'),
            Dense(1)
        ])
        out_model.compile(optimizer='adam', loss='mse')
        out_model.fit(X_scaled, y_out, epochs=200, batch_size=2, verbose=0)
        out_pred = float(out_model.predict(scaler.transform([[14]]), verbose=0)[0][0])
        
        # Metrics
        avg_gain = data['efficiency_gain'].mean()
        avg_cost_reduction = data['cost_reduction'].mean()
        avg_survival = data.get('survival_rate', pd.Series([0])).mean()
        
        recommendation = "Increase training hours to 14+ for optimal efficiency and outcomes" if eff_pred > avg_gain else "Optimize current training process"
        
        insights = (
            f"Analysis of {len(data)} records: avg efficiency {avg_gain:.1f}%, "
            f"avg cost reduction {avg_cost_reduction:.1f}%, "
            f"avg survival rate {avg_survival:.1f}% (prostate-specific), "
            f"NN predicts efficiency {eff_pred:.1f}% for 14 hours, "
            f"NN predicts outcome {out_pred:.1f}% improvement. "
            f"Recommendation: {recommendation}."
        )
        return {"topic": hypothesis["topic"], "insights": insights}