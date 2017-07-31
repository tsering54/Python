from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '\x86c\xb6+f\xb3v\x92\x00\xb7\xe8N\x816V*\xc9\x9e\xf5sQ\xcb\x1e3'
app.count=0

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=1
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
