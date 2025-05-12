from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
@app.route('/h')
def index3():
    return render_template('h.html')


app.run(debug=True, port=8080)
