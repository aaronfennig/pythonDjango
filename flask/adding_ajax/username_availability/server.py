from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "kiskis"

#-----------------------------GET-------------------------------------
@app.route("/")
def index():
    mysql = connectToMySQL("users_db")
    query = "select * from users"
    users = mysql.query_db(query)
    print(users)
    session["numUsers"] = len(users)
    print(session["numUsers"])
    return render_template("index.html")

@app.route("/usersearch")
def userSearch():
    mysql = connectToMySQL("users_db")
    query = "select concat(users.first_name, ' ', users.last_name) as name from users where concat(users.first_name, ' ', users.last_name) like %%(nm)s;"
    data = {
        "nm": request.args.get('nameInput') + "%"
    }
    print("************",data["nm"])
    result = mysql.query_db(query, data)
    print("************results are:*******************", result, "*******************************")
    return render_template("partials/suggestions.html", result = result)

#-----------------------------POST--------------------------------------
@app.route("/postnewuser", methods = ["POST"])
def postNewUser():
    mysql = connectToMySQL("users_db")
    query = "insert into users (first_name, last_name, email) values (%(fn)s, %(ln)s, %(em)s);"
    data = {
        "fn": request.form["firstNameInput"],
        "ln": request.form["lastNameInput"], 
        "em": request.form["emailInput"]
    }
    newUser = mysql.query_db(query, data)
    return redirect("/")

@app.route("/isemailindb", methods = ["POST"])
def isEmailInDB():
    found = False
    mysql = connectToMySQL("users_db")
    query = "select email from users where users.email = %(em)s;"
    data = {
        "em": request.form["emailInput"]
    }
    result = mysql.query_db(query, data)
    print(result)
    if result:
        found = True
    return render_template("partials/email.html", found = found)

if __name__ == "__main__":
    app.run(debug = True)

    