from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result/<userID>")
def result(userID):
    mysql = connectToMySQL("dojo_survey_db")
    query = "select * from users where id = %(id)s"
    data = {
        "id": userID
    }
    user = mysql.query_db(query, data)
    return render_template("result.html", template_user = user)

@app.route("/submitInfo", methods = ["POST"])
def createUser():
    mysql = connectToMySQL("dojo_survey_db")
    query = "insert into users (name, location, language) values (%(nam)s, %(loc)s, %(lng)s)"
    data = {
        "nam": request.form["fullName"],
        "loc": request.form["dojoLocation"],
        "lng": request.form["favoriteLanguage"]
    }

    is_valid = True
    if len(request.form["fullName"]) < 3:
        is_valid = False
        flash("Please enter a valid name!")
    if len(request.form["dojoLocation"]) < 3 or request.form["dojoLocation"] == "---------":
        is_valid = False
        flash("Please enter a valid location!")
    if len(request.form["favoriteLanguage"]) < 2 or request.form["favoriteLanguage"] == "---------":
        is_valid = False
        flash("Please enter a valid language!")
    if is_valid == False:
        return redirect("/")
    else:
        new_user = mysql.query_db(query, data)
        print(new_user)
        userID = new_user
        return redirect(f"result/{userID}")

if __name__ == "__main__":
    app.run(debug = True)

