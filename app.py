from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

showcase = []
others   = []
data     = {}
bio      = []
def get_them():
    global showcase, others,data
    base = ''
    showcase = ["showcase/"+x for x in os.listdir(base+"static/showcase")]
    others   = ["art/"+x for x in os.listdir(base+"static/art")]

    them = {}
    for f in others:
        path = os.path.join(base+"static/", f)
        if os.path.isdir(path):
            folder = "".join(f.split("/")[-1])
            them[folder] = []
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
                        print(name)
                        d_file = open(os.path.join(path,name+".txt"),'r')
                        title  = d_file.readline().strip()
                        desc   = d_file.read().strip().replace("\n", " ")
                        d_file.close()
                        print("TIT", title)
                        print("DSC", desc)
                    grouped = {"img":img, "title":title, "desc":desc}
                    them[folder].append(grouped)
                    data["static/"+img] = grouped

    others   = them
    f = open("static/bio.txt","r")
    
    curr_bio = ""
    for line in f.readlines():
        temp = line.strip()
        if not temp:
            pass
@app.route("/")
def index():
    return render_template("index.html",big=showcase[0],showcase=showcase[1:], others=others,data=data)

get_them()
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
