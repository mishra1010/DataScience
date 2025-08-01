from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'auijhfdkldfmjdpoju'

@app.route('/', methods=['GET', 'POST'])
def home():
    flash('Thanks from Flask App!')
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    flash('Flash again!')
    return render_template('about.html')

app.run(debug=True)