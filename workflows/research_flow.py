from agents.professor import ResearchProfessor
from agents.analyst import ResearchAnalyst
from agents.writer import ResearchTechnicalWriter

def research_workflow(topic: str):
    print(f"Starting research on: {topic}\n")
    
    # Initialize agents
    professor = ResearchProfessor()
    analyst = ResearchAnalyst()
    writer = ResearchTechnicalWriter()
    
    # Research process
    print(f"{professor.name} ({professor.role}) is ready to contribute!")
    hypothesis = professor.develop_hypothesis(topic)
    print(f"Hypothesis v{hypothesis['version']}: {hypothesis['hypothesis']}\n")
    
    print(f"{analyst.name} ({analyst.role}) is ready to contribute!")
    analysis = analyst.analyze_data(hypothesis)
    print(f"Insights: {analysis['insights']}\n")
    
    print(f"{professor.name} ({professor.role}) is ready to contribute!")
    refined_hypothesis = professor.review_analysis(hypothesis, analysis)
    print(f"Refined Hypothesis v{refined_hypothesis['version']}: {refined_hypothesis['hypothesis']}\n")
    
    print(f"{writer.name} ({writer.role}) is ready to contribute!")
    report = writer.write_report(refined_hypothesis, analysis)
    writer.draft_user_guide(topic)
    writer.publish(topic)
    print("Report:")
    print(report)
    
    return report  # Return report for Flask 
