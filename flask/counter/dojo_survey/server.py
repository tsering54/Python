from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key='this is secret'
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/create', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name']= request.form['name']
   session['location']= request.form['location']
   session['language']= request.form['language']
   session['comment']= request.form['comment']
   # redirects back to the '/' route
   return redirect('/result')

@app.route('/result')
def result():
    return render_template('results.html')


app.run(debug=True)
