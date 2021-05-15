from typing import Dict
import pymongo
from flask import Flask,request,render_template
import requests
app = Flask(__name__)
entries = pymongo.MongoClient("mongodb+srv://Recurseform:recurseform@cluster0.arok8.mongodb.net/test")
mydb = entries["Appcode"]
mycol2 = mydb["Answerq1"]


@app.route('/',methods = ["GET","POST"])
def hello_world():
    if(request.method=="POST"):
        code = request.form.get("Appcode")
        option1 = request.form.get("Answerq1")
        option2 = request.form.get("Answerq2")
        option3 = request.form.get("Answerq3")
        option4 = request.form.get("Answerq4")
        option5 = request.form.get("Answerq5")
        option6 = request.form.get("Answerq6")
        option7 = request.form.get("Answerq7")
        option8 = request.form.get("Answerq8")
        option9 = request.form.get("Answerq9")
        option10 = request.form.get("Answerq10")
        option11= request.form.get("Answerq11")
        option12= request.form.get("Answerq12")
        option13= request.form.get("Answerq13")
        option14= request.form.get("Answerq14")
        option15= request.form.get("Answerq15")
        option16= request.form.get("Answerq16")
        option17= request.form.get("Answerq17")
        option18= request.form.get("Answerq18")
        option19= request.form.get("Answerq19")
        option20= request.form.get("Answerq20")


        mycol2.insert_one({"code":code,"option1":option1,"option2":option2,"option3":option3,"option4":option4,"option5":option5,"option6":option6,"option7":option7,"option8":option8,"option9":option9,"option10":option10,"option11":option11,"option12":option12,"option13":option13,"option14":option14,"option15":option15,"option16":option16,"option17":option17,"option18":option18,"option19":option19,"option20":option20})
        return "sucessful"
        
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)