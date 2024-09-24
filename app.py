from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To enable cross-origin requests

# Load pre-trained transformer model for Question-Answering
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Context for the transformer (scraped data)
context = """
St. Xavier's College, Mumbai

Contact Information:
- Phone Number: +91-22-22620661
- Email: examination.centre@xaviers.edu
- Address: St. Xavier's College, Mumbai, India

Visiting Hours:
- Monday to Friday: 10:30 AM to 12:30 PM

Notices:
1. Change of Holiday
2. Attendance Defaulters List up to 31st August 2024 for Odd Semester Exam October 2024
3. Notification for Change in Nomenclature from BMS (Bachelor of Management Studies) to Bachelor of Commerce in Management Studies
4. Ph.D. Degree in Economics Notice
5. Ph.D. Degree in Economics Notice Application
6. Certificate Course in Environmental Forensics
7. Certificate Course in Forensic Biology

Examination Centre: examination.centre@xaviers.edu
"""

# Route for chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_query = request.json.get('query')
    
    # Use transformer to answer the user's question based on context
    qa_input = {
        'question': user_query,
        'context': context
    }
    
    # Get answer from the QA model
    answer = qa_pipeline(qa_input)
    
    return jsonify({
        "question": user_query,
        "answer": answer['answer']
    })

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
