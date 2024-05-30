from flask import Flask, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Use a real secret key in production
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Sample data for admission info
admission_data = {
    "procedures": "To apply for admission, fill out the application form on our website and submit it along with all required documents.",
    "requirements": "The admission requirements include a high school diploma, SAT or ACT scores, and two recommendation letters.",
    "deadlines": "The application deadline for the fall semester is June 1st. For spring semester, the deadline is November 1st."
}

# Function to handle admission-related queries
def get_admission_info(query, context):
    if "procedure" in query.lower() or "how to apply" in query.lower():
        return admission_data["procedures"]
    elif "requirement" in query.lower() or "eligibility" in query.lower():
        return admission_data["requirements"]
    elif "deadline" in query.lower() or "when to apply" in query.lower():
        return admission_data["deadlines"]
    else:
        return None

# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    context = session.get('context', {})

    response = get_admission_info(user_input, context)

    if response:
        session['context'] = context  # Optionally update context here as needed
        return jsonify({"response": response})
    else:
        return jsonify({"response": "I'm sorry, I don't have information about that. Can you ask something else about admission procedures, requirements, or deadlines?"})

# Main function to run the app
if __name__ == "__main__":
    app.run(debug=True)
