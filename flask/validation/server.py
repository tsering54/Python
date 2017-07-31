from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='this_is_secret'
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    if len(request.form['email'])<1:
        flash('email cannot be left blank')
        return redirect('/')
    elif not email_regex.match(request.form['email']):
        flash('email is not valid')
        return redirect('/')

    if len(request.form['fname'])<1:
        flash('fname cannot be left blank')
        return redirect('/')
    elif not request.form['fname'].isalpha():
        flash('not a valid name')
        return redirect('/')

    if len(request.form['lname'])<1:
        flash('lname cannot be left blank')
        return redirect('/')
    elif not request.form['lname'].isalpha():
        flash('not a valid name')
        return redirect('/')

    if len(request.form['pw'])<9:
        flash('password should be more than 8 chars')
        return redirect('/')

    if request.form[pw] != request.form['confirm']:
        flash('passwords do not match')
        return redirect('/')

    flask('sucess')
    return redirect('/')

app.run(debug=True)
