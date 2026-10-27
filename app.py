from flask import Flask,render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os as os

app = Flask("__main__")
load_dotenv()
url=os.getenv("MONGO_URI")
client = MongoClient(url)
db=client['SampleDb']
users=db['SampleDb']



@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/next", methods=['GET','POST'])


def SecondPage():
    name=request.form.get("name").strip()
    phoneNo=request.form.get("phoneNo").strip()

    if not (name and phoneNo) :
        return render_template("index.html",error="Fields Can't be Empty")
    if not name.replace(" ","").isalpha() :
        return render_template("index.html",error="Name should contain only Alphabets")
    if not (phoneNo.isdigit() and len(phoneNo)==10):
        return render_template("index.html",error="Phone No should conatain only Numbers and should be of 10 digits")
    
    users.insert_one({
            "name":name,
            "phoneNo":phoneNo
        })
    
    return render_template("next.html")
    

if __name__ == "__main__":
    app.run(debug=True)