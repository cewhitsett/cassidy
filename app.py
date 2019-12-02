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
    print(showcase)
    return render_template("home.html",big=showcase[0],showcase=showcase[1:], others=others)

if __name__ == "__main__":
    get_them()
    app.run(debug=True)
