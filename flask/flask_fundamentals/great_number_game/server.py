from flask import Flask, render_template, request, redirect, session, flash
import random
import re
Regex = re.compile(r'^[1-9][0-9]?|100$')

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

#---------------------GET-------------------------------
@app.route("/")
def index():
    if "rand" in session:
        pass
    else:
        rand = random.randint(1,100)
        session["rand"] = rand
    print(session)
    return render_template("index.html")

@app.route("/high")
def highGuess():
    return render_template("/high.html")

@app.route("/low")
def lowGuess():
    return render_template("/low.html")

@app.route("/winner")
def winner():
    return render_template("/winner.html")

@app.route("/reset")
def resetGame():
    if "numGuesses" in session:
        session.pop("numGuesses")
    if "rand" in session:
        session.pop("rand")
    if "userGuesses" in session:
        session.pop("userGuess")
    return redirect("/")

@app.route("/lose")
def youLose():
    return render_template("lose.html")

@app.route("/cheat")
def cheater():
    return render_template("cheat.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("/leaderboard.html")

#-----------------POST-----------------------------------
@app.route("/guess", methods = ["POST"])
def userGuess():
    print(session)
    if "numGuesses" in session:
        session["numGuesses"] += 1
    else:
        session["numGuesses"] = 1
    session["userGuess"] = request.form["userGuess"]
    if not Regex.match(session["userGuess"]):
        flash("You've wasted one guess by answering outside the range 1-100")
    if int(session["userGuess"]) > int(session["rand"]) and session["numGuesses"] < 5:
        return redirect("/high")
    elif int(session["userGuess"]) < int(session["rand"]) and session["numGuesses"] < 5:
        return redirect("/low")
    elif int(session["userGuess"]) != int(session["rand"]) and session["numGuesses"] == 5:
        return redirect("/lose")
    elif int(session["userGuess"]) != int(session["rand"]) and session["numGuesses"] >= 5:
        return redirect("/cheat")
    elif int(session["userGuess"]) == int(session["rand"]) and session["numGuesses"] > 5:
        return redirect("/cheat")
    else:
        return redirect("/winner")

@app.route("/leaderboardPost", methods = ["POST"])
def leaderboardPost():
    player = {"name": request.form["name"], "attempts": session["numGuesses"]}
    if "leaderboard" in session:
        print(player)
        session["leaderboard"].append(player)
    else:
        session["leaderboard"] = []
        session["leaderboard"].append(player)
    print(session["leaderboard"])
    return redirect("/leaderboard")


if __name__ == "__main__":
    app.run(debug = True)
