from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "registrationdb")
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
        query =  "INSERT INTO users(first_name, last_name, email, pw_hash, created_at) VALUES(:first_name, :last_name, :email, :password, NOW())"
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
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            # login user
            session['id'] = user[0]['id']
            return redirect('/profile')

    # set flash error message and redirect to login page
    flash('invalid email or password')
    return redirect('/')

@app.route('/profile')
def login():
    if 'id' in session:
        query = "SELECT * FROM users where id=:id"
        data = {
            'id':session['id']
        }
        user_info = mysql.query_db(query, data)[0]
        session['first_name'] = user_info['first_name']
        session['last_name'] = user_info['last_name']
        session['email'] = user_info['email']
        return render_template('profile.html')
    else:
        return rendirect('/')

@app.route('/logout', methods=['POST'])
def logout:
    session.clear()
    return redirect('/')

app.run(debug=True)
