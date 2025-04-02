from agents.professor import ResearchProfessor
from agents.analyst import ResearchAnalyst
from agents.writer import ResearchTechnicalWriter

def research_workflow(topic: str):
    professor = ResearchProfessor()
    analyst = ResearchAnalyst()
    writer = ResearchTechnicalWriter()

    print(professor.report_status())
    hypothesis = professor.develop_hypothesis(topic)
    print(f"Hypothesis v{hypothesis['version']}: {hypothesis['hypothesis']}\n")

    print(analyst.report_status())
    analysis = analyst.analyze_data(hypothesis)
    print(f"Insights: {analysis['insights']}\n")

    print(professor.report_status())
    refined_hypothesis = professor.review_analysis(hypothesis, analysis)
    print(f"Refined Hypothesis v{refined_hypothesis['version']}: {refined_hypothesis['hypothesis']}\n")

    print(writer.report_status())
    report = writer.write_report(refined_hypothesis, analysis)
    writer.draft_user_guide(refined_hypothesis['topic'])
    writer.publish(refined_hypothesis['topic'])
    print(f"Report:\n{report}")