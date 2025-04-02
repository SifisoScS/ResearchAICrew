from core.base_agent import ResearchAgent
import time
import requests
import os
import re
import xml.etree.ElementTree as ET

class ResearchProfessor(ResearchAgent):
    def __init__(self):
        super().__init__("Prof. AI", "Research Professor", 7)

    def fetch_external_data(self, topic: str) -> str:
        print(f"{self.name}: Conducting exploratory study for '{topic}'...")
        time.sleep(1)
        try:
            # Query PubMed via E-utilities
            search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            params = {"db": "pmc", "term": f"{topic} machine learning", "retmax": 1, "retmode": "xml"}
            response = requests.get(search_url, params=params, timeout=5)
            response.raise_for_status()
            root = ET.fromstring(response.text)
            id_elem = root.find(".//Id")
            if id_elem is None:
                return f"No recent ML studies found for {topic}."
            pmc_id = id_elem.text
            
            # Fetch article summary
            fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            fetch_params = {"db": "pmc", "id": pmc_id, "retmode": "xml"}
            fetch_response = requests.get(fetch_url, params=fetch_params, timeout=5)
            fetch_root = ET.fromstring(fetch_response.text)
            title_elem = fetch_root.find(".//Item[@Name='Title']")
            title = title_elem.text if title_elem is not None else "Healthcare ML study found."
            # Check if topic is in title, fallback if not
            return title if topic.lower() in title.lower() else f"ML study related to {topic}"
        except Exception as e:
            return f"Error fetching PubMed data: {str(e)}"

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
        return f"Collaboration Proposal: Partner with healthcare experts to advance {topic} research."

    def execute_research_plan(self, hypothesis: dict) -> str:
        print(f"{self.name}: Executing research plan step for '{hypothesis['topic']}'...")
        time.sleep(1)
        step = hypothesis["research_plan"][0]
        summary = f"Summary of '{step}': Reviewed 10 studies, found ML improves {hypothesis['topic']} efficiency by 15-25%."
        with open("data/output/research_plan_log.txt", "a") as f:
            f.write(f"{time.ctime()}: {summary}\n")
        print(f"{self.name}: {summary}")
        return summary

    def develop_hypothesis(self, topic: str) -> dict:
        external_insight = self.fetch_external_data(topic)
        self.lead_seminar(topic)
        collab = self.develop_collaboration(topic)
        print(f"External Insight: {external_insight}")
        print(f"Collaboration: {collab}")
        time.sleep(1)
        hypothesis = {
            "topic": topic,
            "hypothesis": f"Can {topic} leverage insights like '{external_insight}' to improve efficiency by 20% with ML?",
            "research_plan": [
                f"Study '{external_insight}' implications",
                f"Implement {topic} research gaps",
                "Propose a supervised ML model"
            ],
            "version": 1
        }
        self.execute_research_plan(hypothesis)
        return hypothesis

    def review_analysis(self, hypothesis: dict, analysis: dict) -> dict:
        print(f"{self.name}: Reviewing analysis for '{hypothesis['topic']}'...")
        time.sleep(1)
        insights = analysis["insights"]
        match = re.search(r"avg efficiency (\d+\.\d+)%", insights)
        if not match:
            raise ValueError(f"{self.name}: Could not extract average efficiency from insights: {insights}")
        avg_gain = float(match.group(1))
        
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