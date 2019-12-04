from flask import Flask, render_template
import os

app = Flask(__name__)


showcase = []
others   = []
def get_them():
    global showcase, others
    showcase = ["showcase/"+x for x in os.listdir("static/showcase")]
    others   = ["art/"+x for x in os.listdir("static/art")]

    them = []
    for i in range(0,len(others),4):
        them.append(others[i:i+4])

    others   = them

@app.route("/")
def index():
    return render_template("home.html",big=showcase[0],showcase=showcase[1:], others=others)

@app.route("/home")
def home():
    return render_template("index.html",big=showcase[0],showcase=showcase[1:], others=others)

@app.route("/home1")
def homer():
    return render_template("index2.html",big=showcase[0],showcase=showcase[1:], others=others)

get_them()
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
