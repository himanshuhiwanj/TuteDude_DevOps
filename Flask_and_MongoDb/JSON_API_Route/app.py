from flask import Flask,jsonify
import json

app=Flask(__name__)

@app.route("/api")
def home():
    with open("templates/BackendTextFile.txt","r") as file :
        content = json.load(file)

    return jsonify(content)

if __name__== "__main__" :
    app.run(debug=True)
