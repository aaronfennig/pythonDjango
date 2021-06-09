from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():

    mysql = connectToMySQL("pets")
    query = "select * from pets"
    pets = mysql.query_db(query)
    print(pets)
    return render_template("index.html", template_pets = pets)


@app.route("/addPet", methods = ["POST"])
def addPet():
    mysql = connectToMySQL("pets")
    query = "insert into pets (name, type) values (%(nm)s, %(tp)s)"
    data = {
        "nm": request.form["nameInput"],
        "tp": request.form["typeInput"]
    }
    mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)