from flask_cors import CORS
from flask import Flask,request,render_template,json,jsonify,send_from_directory
import io
app=Flask(__name__)
global folder
CORS(app)
@app.route("/<model>")
def model(model):
    data=json.load(open(model+"/model.json"))
    return jsonify(data)
@app.route("/<folder>/<binary>")
def load_binary(folder,binary):
    return send_from_directory(folder,binary)
if __name__=="__main__":
    app.run()
