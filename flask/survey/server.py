from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key='this is secret'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['POST'])
def create_user():

    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']

    if len(session['name'])<1:
        flash('name cannot be left blank')
        return redirect('/')
    if len(session['comment'])<1:
        flash('comment cannot be left blank')
        return redirect('/')
    if len(session['comment'])>120:
        flash('comment cannot be longer than 120 chars')
        return redirect('/')

    return render_template('results.html')

app.run(debug=True)
