from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def hello_dojo():
    return "Dojo"

@app.route("/hello/<name>")
def hello(name):
    print(name)
    return "Hello " + name

@app.route("/<repeat>/<givenword>/<repeat_num>")
def repeat_word(repeat, givenword, repeat_num):
    if repeat != "repeat":
        return "Sorry. No response. Try again!"
    else:
        print(givenword * int(repeat_num))
        return givenword * int(repeat_num)

if __name__ == "__main__":
    app.run(debug = True)