from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd


app=Flask(__name__)

model = pickle.load(open("weather.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["POST"])
def predict():
    precipitation=float(request.values["precipitation"])
    temp_max=float(request.values["temp_max"])
    temp_min=float(request.values["temp_min"])
    wind=float(request.values["wind"])

    d_f=pd.DataFrame({"precipitation":[precipitation],"temp_max":[temp_max],"temp_min":[temp_min],"wind":[wind]})
    x = model.predict(d_f)
    if x==1:
       data=("drizzle")
    elif x==2:
       data=("rain")
    elif x==3:
       data=("sunny")
    elif x==4:
       data=(" snow")
    elif x==5:
       data=("fog")
    
    
    if x==1:
       return render_template("result1.html",prediction_text="current weather {}".format(data))
    elif x==2:
       return render_template("result2.html",prediction_text="current weather {}".format(data))
    elif x==3:
       return render_template("result3.html",prediction_text="current weather {}".format(data))
    elif x==4:
       return render_template("result4.html",prediction_text="current weather {}".format(data))
    elif x==5:
       return render_template("result5.html",prediction_text="current weather {}".format(data))

if __name__=="__main__":
    app.run(port=8000)