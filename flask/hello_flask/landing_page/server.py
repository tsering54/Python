
# localhost:5000/    This route should serve a view file called index.html and display a greeting.
# localhost:5000/ninjas    This route should serve a view file called ninjas.html and display information about ninjas.
# localhost:5000/dojos/new    This route should serve a view file called dojos.html and have a form be sent to - action=' '.
# from flask import Flask, render_template, url_for
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase='Hello', times=5)

@app.route('/ninjas')
def test():
    return render_template('ninjas.html')
@app.route('/dojos/new')
def dojos():
	return render_template("dojos.html", phrase="Hello", times=5)


app.run(debug=True)
