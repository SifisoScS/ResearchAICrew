from agents.professor import ResearchProfessor
from agents.analyst import ResearchAnalyst
from agents.writer import ResearchTechnicalWriter
from agents.clinician import ClinicianAgent

def research_workflow(topic: str):
    print(f"Starting research on: {topic}\n")
    
    # Initialize agents
    professor = ResearchProfessor()
    analyst = ResearchAnalyst()
    writer = ResearchTechnicalWriter()
    clinician = ClinicianAgent()
    
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
    
    print(f"{clinician.name} ({clinician.role}) is ready to contribute!")
    clinical_advice = clinician.provide_recommendations(refined_hypothesis, analysis)
    print(f"Clinical Advice: {clinical_advice}\n")
    
    print(f"{writer.name} ({writer.role}) is ready to contribute!")
    report = writer.write_report(refined_hypothesis, analysis)
    writer.draft_user_guide(topic)
    writer.publish(topic)
    print("Report:")
    print(report)
    
    return report, clinical_advice  # Return both for Flask