from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key="slfsdjfalsdjfls"
@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    email = request.form['email']
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email address is the wrong format!", 'email')
    if not request.form['first_name'].isalpha():
        flash("No numbers in names!", "first_name")
    if not (request.form['last_name'].isalpha(), "last_name"):
        flash("No numbers in names!")
    if request.form['password'] != request.form['password_confirm']:
        flash("Passwords don't match.", "password")
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters.", "password")
    if request.form['email'] =="":
        flash("Email is a required field.")
    if request.form['first_name'] =="":
        flash("First Name is a required field.")
    if request.form['last_name'] =="":
        flash("Last Name is a required field.")
    if request.form['password'] =="":
        flash("Password is a required field.")   
    if request.form['password_confirm'] =="":
        flash("Confirm Password is a required field.")      
    if '_flashes' in session.keys():
        return redirect("/")

if __name__=="__main__":
    app.run(debug=True)