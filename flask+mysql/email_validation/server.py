from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'emailsdb')
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'this_is_secret'

@app.route('/')
def index():
    return render_template('index.html')

#validation check
@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    if len(email)<1:
        flash('Email is not valid!')
    elif EMAIL_REGEX.match(email):
        flash('The email address you entered ' + email + ' is a VALID email address! Thank you!')

        #insert into database -- type into query and then insert into db
        query = "INSERT INTO emails(email, created_at, updated_at)VALUES(:email, NOW(), NOW())"
        data = {
                    'email' : email
                }
        mysql.query_db(query, data)
        return redirect('/success')

    else:
        flash('Email is not valid!')

    return redirect('/')

#display the inserted data onto db
@app.route('/success')
def success():
    #select from query what you want to display
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('email.html', all_emails = emails)


app.run(debug=True)
