from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
from datetime import datetime


app = Flask(__name__)
app.secret_key = "kiskis"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#-----------------------------GET-----------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        mysql = connectToMySQL("private_wall_db")
        query0 = "select * from users where id = %(UID)s;"
        data = {
            "UID": session["user"]
        }
        loggedUser = mysql.query_db(query0, data)
        print(loggedUser)
        mysql = connectToMySQL("private_wall_db")
        query = "select * from users where id != %(UID)s;"
        users = mysql.query_db(query, data)
        print(users)
        mysql = connectToMySQL("private_wall_db")
        query2 = "SELECT users.first_name as receiver_first, users.last_name as receiver_last, s.first_name as sender_first, s.last_name as sender_last, messages.message, messages.created_at, messages.id FROM messages JOIN users ON messages.received = users.id JOIN users s ON messages.sent = s.id Where messages.received = %(UID)s"
        messages = mysql.query_db(query2, data)
        print(messages)
        mysql = connectToMySQL("private_wall_db")
        query3 = "SELECT users.first_name as receiver_first, users.last_name as receiver_last, s.first_name as sender_first, s.last_name as sender_last, messages.message, messages.created_at, messages.id FROM messages JOIN users ON messages.received = users.id JOIN users s ON messages.sent = s.id Where messages.sent = %(UID)s"
        sent_messages = mysql.query_db(query3, data)
        print("************************", len(sent_messages))

        return render_template("dashboard.html", template_users = users, template_messages = messages, template_loggedUser = loggedUser, template_sent_messages = sent_messages)
    else:
        return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    print(session)
    return redirect("/")

@app.route("/deletemessage/<messageID>")
def deletePost(messageID):
    if "user" in session:
        mysql = connectToMySQL("private_wall_db")
        query0 = "select * from messages join users on users.id = messages.sent where messages.received = %(UID)s;"
        data0 = {
            "UID": session["user"]
        }
        verify = mysql.query_db(query0, data0)
        print("#################",verify)
        if len(verify) > 0:
            print(verify[0]["received"], session["user"])
            if session["user"] == verify[0]["received"]:
                mysql = connectToMySQL("private_wall_db")
                query = "delete from messages where id = %(mid)s;"
                data = {
                    "mid": messageID
                }
                mysql.query_db(query, data)
                return redirect("/dashboard")
            else:
                return redirect ("/notyours")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/notyours")
def notyours():
    return render_template("/notyours")

#--------------------------POST-------------------------------------------
@app.route("/register", methods = ["POST"])
def register():

    is_valid = True

    if len(request.form["firstName"]) < 2:
        is_valid = False
        flash("Please enter a valid first name!", "register")
    
    if len(request.form["lastName"]) < 2:
        is_valid = False
        flash("Please enter a valid last name!", "register")

    if not EMAIL_REGEX.match(request.form["email"]):
        is_valid = False
        flash("Please enter a valid email!", "register")

    else: 
        mysql = connectToMySQL("private_wall_db")
        query = "select * from users where email = %(em)s;"
        data = {
            "em": request.form["email"]
        }
        result = mysql.query_db(query, data)
        if len(result) > 0:
            is_valid = False
            flash("This email is already in use. Please choose another email.", "register")
    
    if request.form["password"] != request.form["confirmPassword"]:
        is_valid = False
        flash("Please make sure that passwords match!", "register")

    if is_valid == False:
        return redirect("/")

    else:
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        print(pw_hash)
        mysql = connectToMySQL("private_wall_db")
        query = "insert into users (first_name, last_name, email, password) values (%(fn)s, %(ln)s, %(em)s, %(pw)s)"
        data = {
            "fn": request.form["firstName"],
            "ln": request.form["lastName"],
            "em": request.form["email"],
            "pw": bcrypt.generate_password_hash(request.form["password"])
        }
        user = mysql.query_db(query, data)
        session["user"] = user
        print(session)
    return redirect("/dashboard")

@app.route("/login", methods = ["POST"])
def login():
    mysql = connectToMySQL("private_wall_db")
    query = "select * from users where email = %(em)s"
    data = {
        "em": request.form["email"]
    }
    user = mysql.query_db(query, data)
    
    if len(user) == 1:
        if bcrypt.check_password_hash(user[0]["password"], request.form["password"]) == True:
            session["user"] =user[0]["id"]
            print(session)
            return redirect("dashboard")
        else:
            flash("Password Invalid", "login")
            return redirect("/")
    else:
        flash("User is not in our database", "login")
        return redirect("/")

@app.route("/postMessage", methods = ["POST"])
def postMessage():
    mysql = connectToMySQL("private_wall_db")
    query = "insert into messages(message, sent, received) values (%(msg)s, %(snt)s, %(rcvd)s);"
    data = {
        "msg": request.form["message"],
        "snt": session["user"], 
        "rcvd": request.form["received"]
    }
    message = mysql.query_db(query, data)
    print(message)
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug = True)

