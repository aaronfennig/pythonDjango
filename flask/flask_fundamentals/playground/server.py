from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():
    num = 3
    color = "blue"
    return render_template("index.html", num = num, color = color)

@app.route("/play/<x>")
def step_two(x):
    return render_template("index.html", num = int(x))

@app.route("/play/<x>/<color>")
def step_three(x, color):
    return render_template("index.html", num = int(x), color = color)

if __name__ == "__main__":
    app.run(debug = True)