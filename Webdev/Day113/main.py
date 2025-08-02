from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'auijhfdkldfmjdpoju'

@app.route('/')
def home():
    name = request.args.get('name', default = 'unnamed')
    lang = request.args.get('lang')
    print(name, lang)
    return render_template('index.html', lang=lang, name=name)


app.run(debug=True)