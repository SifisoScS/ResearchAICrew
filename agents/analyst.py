from core.base_agent import ResearchAgent
import time
import pandas as pd
import os
import requests
from sklearn.tree import DecisionTreeRegressor

class ResearchAnalyst(ResearchAgent):
    def __init__(self):
        super().__init__("Analyst AI", "Research Analyst", 10)

    def fetch_prostate_cancer_data(self, topic: str) -> pd.DataFrame:
        print(f"{self.name}: Fetching topic-specific data for '{topic}'...")
        if "prostate cancer" in topic.lower():
            # Mock SEER-like data for now (replace with real API later)
            data = pd.DataFrame({
                'training_hours': [10, 12, 15, 11, 13],
                'efficiency_gain': [18, 20, 22, 19, 21],
                'outcome_improvement': [85, 88, 92, 87, 90],
                'cost_reduction': [5, 6, 8, 5.5, 7],
                'survival_rate': [90, 92, 95, 91, 93]  # Prostate cancer-specific metric
            })
            # Real SEER API call (commented for now)
            # url = "https://api.seer.cancer.gov/rest/data?query=prostate_cancer"
            # response = requests.get(url, headers={"Authorization": "Bearer YOUR_API_KEY"})
            # data = pd.DataFrame(response.json())
            return data
        return pd.read_csv("data/input/healthcare_data.csv")  # Fallback

    def analyze_data(self, hypothesis: dict) -> dict:
        print(f"{self.name}: Processing dataset for '{hypothesis['topic']}'...")
        time.sleep(2)
        data = self.fetch_prostate_cancer_data(hypothesis['topic'])
        
        avg_gain = data['efficiency_gain'].mean()
        avg_cost_reduction = data['cost_reduction'].mean()
        avg_survival = data.get('survival_rate', pd.Series([0])).mean()  # Prostate-specific
        
        # Topic adjustment
        topic = hypothesis['topic'].lower()
        if "cancer" in topic:
            data['efficiency_gain'] *= 1.1
            data['outcome_improvement'] *= 1.05
        
        # Recalculate averages
        avg_gain = data['efficiency_gain'].mean()
        
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
        
        with open("data/output/model_log.txt", "a") as f:
            f.write(f"{time.ctime()}: Efficiency DT - R²={eff_r_squared:.2f}, Outcome DT - R²={out_r_squared:.2f}\n")
        
        recommendation = "Increase training hours to 14+ for optimal efficiency and outcomes" if eff_pred > avg_gain else "Optimize current training process"
        
        insights = (
            f"Analysis of {len(data)} records: avg efficiency {avg_gain:.1f}%, "
            f"avg cost reduction {avg_cost_reduction:.1f}%, "
            f"avg survival rate {avg_survival:.1f}% (prostate-specific), "
            f"efficiency DT (R²={eff_r_squared:.2f}) predicts {eff_pred:.1f}% for 14 hours, "
            f"outcome DT (R²={out_r_squared:.2f}) predicts {out_pred:.1f}% improvement. "
            f"Recommendation: {recommendation}."
        )
        return {"topic": hypothesis["topic"], "insights": insights}
