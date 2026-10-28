from flask import Flask,render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri=os.getenv("MONGO_URI")

app=Flask(__name__)

client=MongoClient(uri)
db=client["Sample_Todo"]
collection=db["Sample_Todo"]

client.admin.command("ping")

@app.route("/submittodoitem" , methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/data" , methods=['GET','POST'])
def submitData() :
    Item_Name=request.form.get("Item_Name")
    Description=request.form.get("Description")

    collection.insert_one({
        "Item_Name":Item_Name,
        "Description":Description
    })
    return "Data submitted successfully"

if __name__=="__main__":
    app.run(debug="true")
