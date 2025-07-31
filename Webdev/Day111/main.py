from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

app.run(debug=True)