from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "47jfdf9kfdkl9"

@app.route('/')
def index():
    count = 0
    session['count'] = count       
    return redirect("/add")

@app.route('/add')
def add():
    count = session['count']
    session['count'] = count + 1
    print(session['count'])
    return render_template('add.html')

@app.route('/addtwo')
def addtwo():
    count = session['count']
    session['count'] = count + 1
    print(session['count'])
    return redirect('/add')

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True) 