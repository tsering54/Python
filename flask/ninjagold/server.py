from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='this_is_secret' 
import random
import datetime
from datetime import datetime

@app.route('/')
def index():
    if not('gold' in session and 'log' in session):
        session['gold']=0
        session['log']=[]
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building=request.form['building']
    earned_gold=0

    if building == 'farm':
        earned_gold = random.randint(10,20)
    elif building == 'cave':
        earned_gold = random.randint(5,10)
    elif building == 'house':
        earned_gold = random.randint(2,5)
    elif building == 'casino':
        if session['gold']<1:
            session['log'].append('you can not go into the casino if you do not have any gold.({})'.format(datetime.now()))
            return redirect('/')

        earned_gold = random.randint(-50, 50)
        if earned_gold<0:
            if session['gold']-abs(earned_gold)>0:
                session['log'].append('entered a casino and lost {}. ({})'.format(earned_gold, datetime.now()))
            else:
                session['log'].append('entered a casino and lost all of your gold! ({})'.format(datetime.now()))
        else:
            session['log'].append('entered a casino and won {}. ({})'.format(earned_gold, datetime.now()))
        session['gold']+=earned_gold
        return redirect('/')

    session['gold']+=earned_gold
    session['log'].append('earned {} gold from the {}. ({})'. format(earned_gold, building, datetime.now()))
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold')
    session.pop('log')

    return redirect('/')

app.run(debug=True)
