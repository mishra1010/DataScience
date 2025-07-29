from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #return "<p>Hello, World!</p>"
    if request.method == 'POST':
        print(request.form)
        email = request.form['email']
        password = request.form['password']
        print(f"Email: {email}, Password: {password}")
        return "<b>Thanks for using myApp!</b>"
    return render_template('index.html')

app.run(debug=True)
