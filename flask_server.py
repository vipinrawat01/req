from flask import Flask, request, jsonify
from newapp.req import RequirementsAIAssistant
import json
import re
from flask_cors import CORS



def extract_output(result):
    # If result is a CrewOutput object, use .to_dict()
    if hasattr(result, 'to_dict'):
        output = result.to_dict()
        if output:  # If not empty
            return output
        # fallback to .raw if .to_dict() is empty
        if hasattr(result, 'raw'):
            return clean_json_response(result.raw)
    return clean_json_response(result)

def clean_json_response(response):
    # Remove triple quotes and 'json' prefix if present
    if isinstance(response, str):
        # Remove '''json and ''' or ```json and ```
        response = re.sub(r"^[`']{3}json", '', response.strip(), flags=re.IGNORECASE)
        response = re.sub(r"^[`']{3}", '', response.strip())
        response = re.sub(r"[`']{3}$", '', response.strip())
        response = response.strip()
        # Try to load as JSON
        try:
            return json.loads(response)
        except Exception:
            pass  # If not valid JSON, return as is
    return response

app = Flask(__name__)
CORS(app)
assistant = RequirementsAIAssistant()

@app.route('/generate_vision', methods=['POST'])
def generate_vision():
    data = request.get_json()
    result = assistant.generate_vision(inputs=data)
    cleaned = extract_output(result)
    return jsonify(cleaned)

@app.route('/generate_audience', methods=['POST'])
def generate_audience():
    data = request.get_json()
    result = assistant.generate_audience(inputs=data)
    cleaned = extract_output(result)
    return jsonify(cleaned)

@app.route('/generate_features', methods=['POST'])
def generate_features():
    data = request.get_json()
    result = assistant.generate_features(inputs=data)
    cleaned = extract_output(result)
    return jsonify(cleaned)

@app.route('/generate_constraints', methods=['POST'])
def generate_constraints():
    data = request.get_json()
    result = assistant.generate_constraints(inputs=data)
    cleaned = extract_output(result)
    return jsonify(cleaned)

@app.route('/chat_with_assistant', methods=['POST'])
def chat_with_assistant():
    data = request.get_json()
    result = assistant.chat_with_assistant(inputs=data)
    cleaned = extract_output(result)
    return jsonify(cleaned)

if __name__ == '__main__':
    app.run(debug=True) 