from flask import Flask, request, render_template
import markdown
import signal
import sys
from werkzeug.serving import run_simple, WSGIRequestHandler
from workflows.research_flow import research_workflow

print("Starting app.py...")

app = Flask(__name__)
print("Created Flask app")

# Global variable to store the server instance
server = None

# Simple rule-based symptom checker (to be replaced with ML model later)
def analyze_symptoms(symptoms: str, disease: str) -> dict:
    symptoms = symptoms.lower()
    if "prostate cancer" in disease.lower():
        if any(word in symptoms for word in ["frequent urination", "blood in urine", "pelvic pain"]):
            return {"disease": "Prostate cancer", "probability": 0.85, "message": "High likelihood of Prostate cancer detected."}
        else:
            return {"disease": "Prostate cancer", "probability": 0.3, "message": "Low likelihood of Prostate cancer based on symptoms."}
    elif "alzheimer's" in disease.lower():
        if any(word in symptoms for word in ["memory loss", "confusion", "difficulty speaking"]):
            return {"disease": "Alzheimer's", "probability": 0.75, "message": "High likelihood of Alzheimer's disease detected."}
        else:
            return {"disease": "Alzheimer's", "probability": 0.2, "message": "Low likelihood of Alzheimer's based on symptoms."}
    elif "diabetes" in disease.lower():
        if any(word in symptoms for word in ["increased thirst", "frequent urination", "fatigue"]):
            return {"disease": "Diabetes", "probability": 0.8, "message": "High likelihood of Diabetes detected."}
        else:
            return {"disease": "Diabetes", "probability": 0.25, "message": "Low likelihood of Diabetes based on symptoms."}
    return {"disease": disease, "probability": 0.1, "message": "Insufficient data to determine likelihood."}

# Mock file analysis (to be replaced with real analysis later)
def analyze_file(file, disease: str) -> dict:
    if file:
        return {"disease": disease, "probability": 0.9, "message": f"File analysis suggests high likelihood of {disease}."}
    return {"disease": disease, "probability": 0.0, "message": "No file uploaded for analysis."}

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Inside index route")
    if request.method == 'POST':
        symptoms = request.form.get('symptoms', '')
        disease = request.form.get('disease', '')
        file = request.files.get('file')
        
        print(f"Received symptoms: {symptoms}, disease: {disease}, file: {file}")
        
        # Analyze symptoms
        symptom_result = analyze_symptoms(symptoms, disease)
        
        # Analyze file (if uploaded)
        file_result = analyze_file(file, disease)
        
        # Run research workflow for the selected disease
        try:
            report, clinical_advice = research_workflow(disease)
            report_html = markdown.markdown(report)
            advice_html = markdown.markdown(clinical_advice)
            plot_path = f"static/{disease.replace(' ', '_')}_multi_metric_plot.png"
            print("Rendering result.html")
            return render_template('result.html', 
                                 report_html=report_html, 
                                 advice_html=advice_html, 
                                 plot_path=plot_path,
                                 symptom_result=symptom_result,
                                 file_result=file_result)
        except Exception as e:
            error_html = markdown.markdown(f"**Error**: {str(e)}")
            print(f"Error occurred: {str(e)}")
            return render_template('result.html', 
                                 report_html=error_html, 
                                 advice_html="", 
                                 plot_path=None,
                                 symptom_result=symptom_result,
                                 file_result=file_result)
    print("Rendering index.html")
    return render_template('index.html')

# Placeholder routes for navbar links
@app.route('/diagnosis')
def diagnosis():
    return "Diagnosis page (coming soon)"

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/find-doctor')
def find_doctor():
    return render_template('find_doctor.html')

@app.route('/logout')
def logout():
    return "Logout page (coming soon)"

def shutdown_server(signum, frame):
    print("\nShutting down Flask server gracefully...")
    if server:
        server.shutdown()
    sys.exit(0)

if __name__ == '__main__':
    print("Registering signal handler")
    signal.signal(signal.SIGINT, shutdown_server)
    print("Starting Flask server on http://localhost:5000")
    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)