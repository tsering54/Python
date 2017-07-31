from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create():
    #create a dictionary
    query = 'insert into friends(first_name, last_name, occupation, created_at, updated_at)values(:first_name, :last_name, :occupation, now(), now())'
    #get data from user
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],

           }
    mysql.query_db(query, data)
    return redirect('/')



app.run(debug=True)
