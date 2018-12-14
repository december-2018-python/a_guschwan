from flask import Flask, render_template, request, redirect, session, Markup
import random, datetime
app = Flask(__name__)
app.secret_key = "afjasfkja87"
@app.route('/', methods=["get","post"])

def index():
        
    add = 0
        
        #message = []

    if 'add' not in session:
        session['num']=0
         #   session['add']=0
            #message = []
       # else:
        #    if session['add'] > 0:
        #        tmp = session['message'] 
        #        message.append("<p class='green'>Earned " + str(session['add']) + " golds from the " + session['place'] + "  " + "(" + str(datetime.datetime.now()) + ")</p>")
        #        session['message'] = str(message) + "\n" + tmp 
        #    else:
        #        tmp = session['message'] 
        #        message.append("Entered a casino and lost " + str(session['add']) + " golds... Ouch." + "  " + "(" + str(datetime.datetime.now()) + ")")
        #        session['message'] = str(message) + "\n" + tmp
        
        return render_template("index.html")

@app.route('/process_money', methods=["get","post"])
def process_money():
    session['message'] = []
    if request.form['building'] == 'farm':
        num = random.randrange(10,20)
        if session['num'] == 0:
            session['message'] = []
        session['place'] = 'farm'
    elif request.form['building'] == 'house':
        num = random.randrange(2,5)
        session['place'] = 'house'
        if session['num'] == 0:
            session['message'] = []
    elif request.form['building'] == 'cave':
        num = random.randrange(5,10)
        session['place'] = 'cave'
        if session['num'] == 0:
            session['message'] = []
    elif request.form['building'] == 'casino':
        num = random.randrange(-50,50)
        session['place'] = 'casino'
        if session['num'] == 0:
            session['message'] = []
    
    session['add'] = num
    session['num'] = session['num'] + num
    #message = "<p class='green'>Earned " + str(session['add']) + " golds from the " + session['place'] + "  " + "(" + str(datetime.datetime.now()) + ")</p>"
    session['message'].append("<p class='green'>Earned " + str(session['add']) + " golds from the " + session['place'] + "  " + "(" + str(datetime.datetime.now()) + ")</p>")
    
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)