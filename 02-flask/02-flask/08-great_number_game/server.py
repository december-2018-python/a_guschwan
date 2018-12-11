from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "afjasfkja87"
@app.route('/', methods=["get","post"])
def index():
    num = random.randrange(0,101)
    session['num'] = num
    print(session['num'])
    return render_template("index.html")

@app.route('/guess', methods=["get","post"])
def guess():
    num = session['num']
    guess = request.form['guess']
    result = ""
    if guess != "":
        if int(guess) > int(num):
            result = "Too high"
        elif int(guess) < int(num):
            result = "Too low"
        elif int(guess) == int(num):
            result = "You got it"
        else:
            result = ""
    
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)