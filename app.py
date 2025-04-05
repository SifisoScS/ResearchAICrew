from flask import Flask, request, render_template
import markdown
import signal
import sys
from werkzeug.serving import run_simple, WSGIRequestHandler

print("Starting app.py...")

from workflows.research_flow import research_workflow
print("Imported research_workflow")

app = Flask(__name__)
print("Created Flask app")

# Global variable to store the server instance
server = None

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Inside index route")
    if request.method == 'POST':
        topic = request.form['topic']
        print(f"Received topic: {topic}")
        try:
            report, clinical_advice = research_workflow(topic)  # Now returns report and advice
            report_html = markdown.markdown(report)
            advice_html = markdown.markdown(clinical_advice)
            plot_path = f"static/{topic.replace(' ', '_')}_multi_metric_plot.png"
            print("Rendering result.html")
            return render_template('result.html', report_html=report_html, advice_html=advice_html, plot_path=plot_path)
        except Exception as e:
            error_html = markdown.markdown(f"**Error**: {str(e)}")
            print(f"Error occurred: {str(e)}")
            return render_template('result.html', report_html=error_html, advice_html="", plot_path=None)
    print("Rendering index.html")
    return render_template('index.html')

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