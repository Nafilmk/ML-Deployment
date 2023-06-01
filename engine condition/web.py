from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd


app=Flask(__name__)

model = pickle.load(open("engine_condition.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["POST"])
def predict():
    Engine_rpm=float(request.values["Engine_rpm"])
    Lub_oil_pressure=float(request.values["Lub_oil_pressure"])
    Fuel_pressure=float(request.values["Fuel_pressure"])
    Coolant_pressure=float(request.values["Coolant_pressure"])
    lub_oil_temp=float(request.values["lub_oil_temp"])
    Coolant_temp=float(request.values["Coolant_temp"])



    d_f=pd.DataFrame({"Engine_rpm":[Engine_rpm],"Lub_oil_pressure":[Lub_oil_pressure],"Fuel_pressure":[Fuel_pressure],"Coolant_pressure":[Coolant_pressure],"lub_oil_temp":[lub_oil_temp],"Coolant_temp":[Coolant_temp]})
    x = model.predict(d_f)
    if x == 0:
       data=("bad condition")
    else :
       data=("good condition")
    
    return render_template("home.html",prediction_text=data)

if __name__=="__main__":
    app.run(port=8000)