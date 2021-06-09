from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
        print(session["counter"])
    else:
        session["counter"] = 1
        print(session["counter"])
    if "actualViews" in session:
        session["actualViews"] +=1
    else:
        session["actualViews"] = 1
    return render_template("index.html", template_counter = session["counter"], template_actual_counter = session["actualViews"])

@app.route("/destroy")
def destroySession():
    # session.clear()
    session.pop("counter")
    session["counter"] = -1
    return redirect("/")

@app.route("/addtwo")
def addTwo():
    session["counter"] +=1
    return redirect("/")

@app.route("/adduserinput", methods = ["POST"])
def addUserInput():
    print(request.form["numInput"])
    session["counter"] += int(request.form["numInput"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)