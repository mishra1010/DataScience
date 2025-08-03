from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    # Some machine learning Model
    data = {"Output": 45, "Accuracy": 98.55}
    return jsonify(data), 200


app.run(debug=True)