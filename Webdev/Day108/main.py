from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', static_url_path='/files')    # static folder on disk is assets here - physical path after this give static url path to override assets

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/about')
# def about():
#     return "<p>Hello, Welcome to the Flask Web Application about!</p>"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

app.run(debug=True)


