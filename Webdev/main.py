from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Hello, Welcome to the Flask Web Application!</p>"

# @app.route('/about')
# def about():
#     return "<p>Hello, Welcome to the Flask Web Application about!</p>"

@app.route('/about')
def about():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return "<p>Hello, Welcome to the Flask Web Application contact!</p>"

app.run(debug=True)


