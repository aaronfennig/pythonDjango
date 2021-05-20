from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():

    return render_template("result.html", name_template = session["name"], location_template= session["location"], language_template = session["language"])

@app.route("/submitInfo", methods = ["POST"])
def createUser():
    session["name"]= request.form["name"]
    session["location"]= request.form["dojoLocation"]
    session["language"] = request.form["favLanguage"]
    return redirect("result")

if __name__ == "__main__":
    app.run(debug = True)

