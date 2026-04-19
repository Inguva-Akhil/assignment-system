from flask import Flask, request, jsonify

app = Flask(__name__)

submissions = []

@app.route('/')
def home():
    return "Assignment System Running"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    if not data.get("name") or not data.get("assignment"):
        return jsonify({"error": "Invalid data"}), 400
    
    submissions.append(data)
    return jsonify({"message": "Submitted successfully"}), 200

@app.route('/all', methods=['GET'])
def all_submissions():
    return jsonify(submissions)

if __name__ == '__main__':
    app.run(debug=True)