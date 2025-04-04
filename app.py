from flask import Flask, request, render_template
from workflows.research_flow import research_workflow

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        try:
            report = research_workflow(topic)  # Returns report string
            return render_template('result.html', report=report)
        except Exception as e:
            return render_template('result.html', report=f"Error: {str(e)}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)