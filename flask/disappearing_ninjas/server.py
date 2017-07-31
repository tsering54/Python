from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key='this_is_secret'

@app.route('/')
def index():
    return 'no ninjas here'

@app.route('/ninja')
def ninjas():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja(color):
    return render_template('index.html', color=color)

app.run(debug=True)
