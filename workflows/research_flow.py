from agents.professor import ResearchProfessor
from agents.analyst import ResearchAnalyst
from agents.writer import ResearchTechnicalWriter

def research_workflow(topic: str):
    professor = ResearchProfessor()
    analyst = ResearchAnalyst()
    writer = ResearchTechnicalWriter()

    print(professor.report_status())
    hypothesis = professor.develop_hypothesis(topic)
    print(f"Hypothesis: {hypothesis['hypothesis']}\n")

    print(analyst.report_status())
    analysis = analyst.analyze_data(hypothesis)
    print(f"Insights: {analysis['insights']}\n")

    print(writer.report_status())
    report = writer.write_report(hypothesis, analysis)
    print(f"Report:\n{report}") 
