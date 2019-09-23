from flask_cors import CORS
from flask import Flask,request,render_template,json,jsonify,send_from_directory
import os
app=Flask(__name__)
global folder
CORS(app)

@app.route("/")
def index():
    files=os.listdir()
    links=[]
    for f in files:
        if not os.path.isfile(f) and f.startswith('model_'):
            links.append("/"+f)
    return render_template('index.html',links=links)

@app.route("/<model>")
def model(model):
    data=json.load(open(model+"/model.json"))
    return jsonify(data)
@app.route("/<folder>/<binary>")
def load_binary(folder,binary):
    return send_from_directory(folder,binary)
if __name__=="__main__":
    app.run()
