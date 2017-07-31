from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "walldb")
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key='secret'


@app.route('/')
def index():
    return render_template('index.html')

#if register is selected
@app.route('/register')
def register():
    return render_template('register.html')


#in register.html, create user
@app.route('/create', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']

    errors = False

    if len(first_name)<2:
        flash('First name should be at least 2 characters')
        errors = True
    if len(last_name)<2:
        flash('Last name should be at least 2 characters')
        errors = True
    if len(email)<1:
        flash('email is not valid')
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash('enter a valid email')
        errors = True

    #check if email exists in db
    query = "SELECT * from users WHERE email=:email"
    data = {
            'email':email
    }
    result = mysql.query_db(query, data)

    if len(result)>0:
        flash('email already exists!')
        errors = True

    if len(password)<8:
        flash('password should be at least 8 characters')
        errors = True

    if password != confirm:
        flash('passwords dont match')
        errors = True

    if errors:
        return redirect('/')

    else:
        enc_pw = bcrypt.generate_password_hash(password)
        query =  "INSERT INTO users(first_name, last_name, email, password, created_at) VALUES(:first_name, :last_name, :email, :password, NOW())"
        data = {
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'password':enc_pw
        }
        mysql.query_db(query, data)
        flash('registration successful!')
        return redirect('/')

#if login is selected -- check if info matches info in db

@app.route('/login', methods=['POST'])
def process():
    email = request.form['email']
    password = request.form['password']

    #check email exists in db to login else redirect to register
    query = "SELECT * from users WHERE email=:email LIMIT 1"
    data = {
            'email':email
    }
    user = mysql.query_db(query, data)

    if user:
        if bcrypt.check_password_hash(user[0]['password'], password):
            # login user
            session['user_id'] = user[0]['id']
            session['first_name'] = user[0]['first_name']
            return redirect('/wall')

    # set flash error message and redirect to login page
    flash('invalid email or password')
    return redirect('/')


@app.route('/wall', methods=['GET'])
def wall():

    message_query = "SELECT messages.id, CONCAT(first_name, ' ', last_name) AS name, messages.message, DATE_FORMAT(messages.created_at, '%M %D %Y') AS date, messages.user_id FROM messages JOIN users on messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(message_query)


    comment_query = "SELECT comments.id, CONCAT(first_name, ' ', last_name) as name, comments.comment, DATE_FORMAT(comments.created_at, '%M %D %Y')AS date, comments.user_id AS user_id, comments.message_id AS message_id FROM comments JOIN messages on comments.message_id = messages.id JOIN users on messages.user_id = users.id ORDER by comments.created_at DESC"
    comments = mysql.query_db(comment_query)

    return render_template('the_wall.html', messages=messages, comments=comments)

@app.route('/message', methods=['POST'])
def message():
    query = "INSERT INTO messages(user_id, message, created_at, updated_at) VALUES(:user_id, :message, NOW(), NOW())"
    data = {
            'user_id': session['user_id'],
            'message': request.form['user_message']
            }
    mysql.query_db(query,data)

    return redirect('/wall')

@app.route('/comment/<id>', methods=['POST'])
def comment(id):
    query = "INSERT INTO comments(message_id, user_id, comment, created_at, updated_at) VALUES(:message_id, :user_id, :comment, NOW(), NOW())"
    data = {
            'message_id': id,
            'user_id': session['user_id'],
            'comment': request.form['user_comment']
           }

    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
