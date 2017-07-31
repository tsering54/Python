from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'thisissecret'
import random

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    if 'rand' not in session:
        session['rand']=random.randint(1,100)

    guess=int(request.form['guess'])

    if guess>session['rand']:
        session['guess']='too_high'
    elif guess<session['rand']:
        session['guess']='too_low'
    else:
        session['guess']='correct'
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
