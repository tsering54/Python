from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '\x86c\xb6+f\xb3v\x92\x00\xb7\xe8N\x816V*\xc9\x9e\xf5sQ\xcb\x1e3' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

@app.route('/')
def index():
  return render_template("index.html", name='Jay', email='kpatel@codingdojo.com')

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # notice how the key we are using to access the info corresponds with the names
   # of the inputs from our html form
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # redirects back to the '/' route

@app.route('/show')
def show_user():
  return render_template('index.html', name=session['name'], email=session['email'])


app.run(debug=True)
