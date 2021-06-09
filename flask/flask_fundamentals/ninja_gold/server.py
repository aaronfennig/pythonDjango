from flask import Flask, render_template, request, redirect, session, flash
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


#-----------------------------GET----------------------------------
@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    if "gold" in session:
        pass
    else:
        session["gold"] = 0
    if int(session["counter"]) == 16 and int(session["gold"]) < 195:
        return redirect("/lose")
    if int(session["counter"]) < 16 and int(session["gold"]) >= 195:
        return redirect ("/win")
    return render_template("index.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/lose")
def lose():
    session.clear()
    return render_template("lose.html")

@app.route("/win")
def win():
    session.clear()
    return render_template("win.html")


#-----------------------------POST--------------------------------

@app.route("/postActivity", methods = ["POST"])
def postActivity():
    if "listOfEvents" in session:
        pass
    else:
        session["listOfEvents"] = []
    randFarm = random.randint(10, 20)
    randCave = random.randint(5, 10)
    randHouse = random.randint(2, 5)
    randCasino = random.randint(0, 50)
    if request.form["whichActivity"] == "farm":
        Event = {"location": request.form["whichActivity"], "amount": randFarm, "time": datetime.now().strftime("%c")}
        session["listOfEvents"].append(Event)
        session["gold"] += int(randFarm)
    elif request.form["whichActivity"] == "cave":
        Event = {"location": request.form["whichActivity"], "amount": randCave, "time": datetime.now().strftime("%c")}
        session["listOfEvents"].append(Event)
        session["changeAmount"] = randCave
        session["gold"] += int(randCave)
    elif request.form["whichActivity"] == "house":
        Event = {"location": request.form["whichActivity"], "amount": randHouse, "time": datetime.now().strftime("%c")}
        session["listOfEvents"].append(Event)
        session["changeAmount"] = randHouse
        session["gold"] += int(randHouse)
    else:
        rand5050 = random.randint(0, 1)
        print("casino results are: ", rand5050)
        if rand5050 == 1:
            session["changeAmount"] = randCasino
            session["gold"] += int(randCasino)
        else:
            session["changeAmount"] = -randCasino
            session["gold"] -= int(randCasino)
        Event = {"location": request.form["whichActivity"], "amount": randCasino,"didWin":int(rand5050), "time": datetime.now().strftime("%c")}
        session["listOfEvents"].append(Event)
    print(session)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)