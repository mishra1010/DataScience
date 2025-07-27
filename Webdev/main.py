from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Hello, Welcome to the Flask Web Application!</p>"


app.run(debug=True)


