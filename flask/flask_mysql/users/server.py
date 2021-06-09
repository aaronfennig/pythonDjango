from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)

#--------------------Get Routes------------------------------
@app.route("/users")
def index():
    mysql = connectToMySQL("users_db")
    query = "select * from users"
    users = mysql.query_db(query)
    print(users)
    return render_template("index.html", template_users = users)

@app.route("/users/new")
def addUser():
    return render_template("addUser.html")

@app.route("/users/<userID>")
def oneUser(userID):
    mysql = connectToMySQL("users_db")
    query = "select * from users where user_id = %(UID)s;"
    data = {
        "UID": userID
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("oneUser.html", template_user = user)

@app.route("/users/<userID>/edit")
def editUser(userID):
    mysql = connectToMySQL("users_db")
    query = "select * from users where user_id = %(UID)s;"
    data = {
        "UID": userID
    }
    user = mysql.query_db(query, data)
    return render_template("editUser.html", template_user = user)

@app.route("/users/<userID>/delete")
def deleteUser(userID):
    mysql = connectToMySQL("users_db")
    query = "delete from users where user_id = %(UID)s;"
    data = {
        "UID": userID
    }
    mysql.query_db(query, data)
    return redirect("/users")

#-------------------------Post Routes---------------------
@app.route("/users/postnewuser", methods = ["POST"])
def postNewUser():
    mysql = connectToMySQL("users_db")
    query = "insert into users(first_name, last_name, email) values(%(fn)s, %(ln)s, %(em)s);"
    data = {
        "fn": request.form["firstNameInput"],
        "ln": request.form["lastNameInput"],
        "em": request.form["emailInput"]
    }
    newUser = mysql.query_db(query, data)
    return redirect(f"/users/{newUser}")

@app.route("/users/<userID>/edit/update", methods = ["POST"])
def editUserPost(userID):
    mysql = connectToMySQL("users_db")
    query = "update users_db.users set first_name = %(fn)s, last_name = %(ln)s, email = %(em)s where user_id = %(UID)s;"
    data = {
        "UID": userID,
        "fn": request.form["firstNameInput"],
        "ln": request.form["lastNameInput"],
        "em": request.form["emailInput"]
    }
    newUser = mysql.query_db(query, data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug = True)