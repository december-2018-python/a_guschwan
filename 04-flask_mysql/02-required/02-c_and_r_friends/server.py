from flask import Flask, render_template, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
@app.route('/')
def index():
    mysql = connectToMySQL('friendsdb')
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends = all_friends)
    
@app.route('/create/friend', methods=["post"])
def create():
    mysql = connectToMySQL('friendsdb')
    query ="INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) values (%(fname)s, %(lname)s, %(occupation)s, NOW(), NOW())";
    data = {
        "first_name": request_form['fname'],
        "last_name": request_form['lname'],
        "occupation": request_form['occupation']
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')
# now, we may invoke the query_db method
#print("all the users", mysql.query_db("SELECT * FROM users;"))
if __name__ == "__main__":
    app.run(debug=True)