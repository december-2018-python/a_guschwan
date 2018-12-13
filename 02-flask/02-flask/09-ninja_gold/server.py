from flask import Flask, render_template, request, redirect, session, Markup
import random, datetime
app = Flask(__name__)
app.secret_key = "afjasfkja87"
@app.route('/', methods=["get","post"])

def index():
    temp = session['num']
    session['num'] = 0
    session['num'] = temp
    if session['add'] > 0:
        tmp = session['message'] 
        message = "Earned " + str(session['add']) + " golds from the " + session['place'] + "  " + "(" + str(datetime.datetime.now()) + ")"
        session['message'] = message + "\n" + tmp  
    else:
        tmp = session['message'] 
        message = "Entered a casino and lost " + str(session['add']) + " golds... Ouch." + "  " + "(" + str(datetime.datetime.now()) + ")"
        session['message'] = message + "\n" + tmp
    return render_template("index.html", message=message )

@app.route('/process_money', methods=["get","post"])
def process_money():
    num = 0
    if request.form['building'] == 'farm':
        num = random.randrange(10,20)
        session['place'] = 'farm'
    elif request.form['building'] == 'house':
        num = random.randrange(2,5)
        session['place'] = 'house'
    elif request.form['building'] == 'cave':
        num = random.randrange(5,10)
        session['place'] = 'cave'
    else:
        num = random.randrange(-50,50)
        session['place'] = 'casino'
    session['add'] = num
    session['num'] = session['num'] + num   
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)