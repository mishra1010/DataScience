from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = "John Doe"
    lang = "Java"
    luckynos = [1,5,73,25]
    footer = "<p>copyright @2025 | All rights reserved</p>"
    return render_template('index.html',name = name, lang = lang, lucky = luckynos, footer=footer)

app.run(debug=True)