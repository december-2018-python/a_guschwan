from flask import Flask, render_template, request, redirect, session, Markup
import random, datetime
app = Flask(__name__)
app.secret_key = "afjasfkja87"

@app.route('/', methods=["get","post"])
def index():
    try:
        session['num']
    except:
        session['num'] = 0
    return render_template("index.html" )

@app.route('/process_money', methods=["get","post"])
def process_money():
    add = 0
    try:
        session['message']
    except:
        session['message'] =[]

    if request.form['building'] == 'farm':
        add = random.randrange(10,20)
        session['place'] = 'farm'
    elif request.form['building'] == 'house':
        add = random.randrange(2,5)
        session['place'] = 'house'
    elif request.form['building'] == 'cave':
        add = random.randrange(5,10)
        session['place'] = 'cave'
    else:
        add = random.randrange(-50,50)
        session['place'] = 'casino'
    session['num'] += add

    if add > 0:
        session['message'].insert(0, "<p class='green'>" + "Earned " + str(add) + " golds from the " + session['place'] + "  " + "(" + str(datetime.datetime.now()) + ")" + "</p>")
    else: 
        session['message'].insert(0, "<p class='red'>" + "Entered a casino and lost " + str(add) + " golds... Ouch." + "  " + "(" + str(datetime.datetime.now()) + ")" + "</p>") 
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)