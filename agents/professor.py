from core.base_agent import ResearchAgent
import time
import requests
from bs4 import BeautifulSoup
import os

class ResearchProfessor(ResearchAgent):
    def __init__(self):
        super().__init__("Prof. AI", "Research Professor", 7)

    def fetch_external_data(self, topic: str) -> str:
        print(f"{self.name}: Conducting exploratory study for '{topic}'...")
        time.sleep(1)
        try:
            url = "https://techcrunch.com"
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            headline = soup.find('h2', class_='post-block__title')
            return headline.get_text().strip() if headline else "No relevant data found."
        except Exception as e:
            return f"Error fetching data: {str(e)}"

    def lead_seminar(self, topic: str) -> None:
        print(f"{self.name}: Leading seminar on '{topic}'...")
        time.sleep(1)
        guidance = f"Seminar Notes for {topic}: Focus on ML trends and research gaps."
        with open("data/output/seminar_log.txt", "a") as f:
            f.write(f"{time.ctime()}: {guidance}\n")
        print(f"{self.name}: Seminar notes logged.")

    def develop_collaboration(self, topic: str) -> str:
        print(f"{self.name}: Proposing collaboration for '{topic}'...")
        time.sleep(1)
        return f"Collaboration Proposal: Partner with industry experts to advance {topic} research."

    def develop_hypothesis(self, topic: str) -> dict:
        external_insight = self.fetch_external_data(topic)
        self.lead_seminar(topic)
        collab = self.develop_collaboration(topic)
        print(f"External Insight: {external_insight}")
        print(f"Collaboration: {collab}")
        time.sleep(1)
        return {
            "topic": topic,
            "hypothesis": f"Can {topic} leverage insights like '{external_insight}' to improve efficiency by 20% with ML?",
            "research_plan": [
                f"Study '{external_insight}' implications",
                f"Implement {topic} research gaps",
                "Propose a supervised ML model"
            ],
            "version": 1
        }

    def review_analysis(self, hypothesis: dict, analysis: dict) -> dict:
        print(f"{self.name}: Reviewing analysis for '{hypothesis['topic']}'...")
        time.sleep(1)
        insights = analysis["insights"]
        avg_gain = float(insights.split("average ")[1].split("%")[0])
        if avg_gain >= 20:
            refined_hypothesis = f"Can {hypothesis['topic']} consistently achieve {avg_gain:.1f}%+ efficiency with ML?"
            new_plan = hypothesis["research_plan"] + ["Validate with larger dataset"]
        else:
            refined_hypothesis = f"Can {hypothesis['topic']} reach 20% efficiency with optimized ML techniques?"
            new_plan = hypothesis["research_plan"] + ["Optimize ML model parameters"]
        return {
            "topic": hypothesis["topic"],
            "hypothesis": refined_hypothesis,
            "research_plan": new_plan,
            "version": hypothesis["version"] + 1
        }