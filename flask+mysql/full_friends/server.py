from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriendsdb')

#get -- display all friends from query onto index.html page
@app.route('/', methods = ['GET'])
def index():
    query = "SELECT * from friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

#post '/friends' create() , handle add friend form submit and create friend in db
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends(first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(query, data)
    return redirect('/')                #goes back to index and displays it on there


#get    '/friends/<id>/edit'    edit(id)    ,display the edit friend page for particular friend
@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends where id = :specific_id"
    data={
        'specific_id': id
    }
    friend = mysql.query_db(query, data)
    return render_template('friends.html', edit_friend=friend[0])

#update the friend that was edited into db
@app.route('/friends/<id>', methods=['POST'])
def update(id):

    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() where id=:specific_id"
    data = {
            'specific_id':id,
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
    }
    mysql.query_db(query, data)
    return redirect('/')

#deleting a friend from db
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends where id=:specific_id"
    data = {
            'specific_id' : id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug = True)
