from flask import Flask, render_template
import os

app = Flask(__name__)

showcase = []
others   = []
order    = []
def get_them():
    global showcase, others,order
    base = ''
    showcase = ["showcase/"+x for x in os.listdir(base+"static/showcase")]
    others   = ["art/"+x for x in os.listdir(base+"static/art")]

    them = {}
    for f in others:
        path = os.path.join(base+"static/", f)
        if os.path.isdir(path):
            folder = "".join(f.split("/")[-1])
            them[folder] = []
            order.append(folder)
            for subfile in os.listdir(path):
                newpath = os.path.join(f+"/",subfile)
                if not os.path.isdir(newpath):
                    if subfile.endswith(".txt"):
                        continue
                    img = os.path.join("",newpath)
                    title = ""
                    desc = ""
                    name = "".join(subfile.split(".")[:-1])
                    if os.path.exists(os.path.join(path,name+".txt")):
                        d_file = open(os.path.join(path,name+".txt"),'r')
                        title  = d_file.readline().strip()
                        desc   = d_file.read().strip().replace("\n", " ")
                    print(img)
                    them[folder].append({"img":img, "title":title, "desc":desc}) 

    others   = them

@app.route("/")
def index():
    print(others)
    return render_template("index.html",big=showcase[0],showcase=showcase[1:], others=others, order=order)

get_them()
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
