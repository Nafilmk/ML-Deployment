from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd


app=Flask(__name__)

model = pickle.load(open("food category.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["POST"])
def predict():
    Grams=float(request.values["Grams"])
    Calories=float(request.values["Calories"])
    Protein=float(request.values["Protein"])
    Fat=float(request.values["Fat"])
    Sat_fat=float(request.values["Sat_fat"])
    Fiber=float(request.values["Fiber"])
    Carbs=float(request.values["Carbs"])

    d_f=pd.DataFrame({"Grams":[Grams],"Calories":[Calories],"Protein":[Protein],"Fat":[Fat],"Sat_fat":[Sat_fat],"Fiber":[Fiber],"Carbs":[Carbs]})
    x = model.predict(d_f)
    if x==1:
      data=("Dairy products")
    elif x==2:
      data=("Fats, Oils, Shortenings")
    elif x==3:
      data=("Meat, Poultry")
    elif x==4:
      data=(" Fish, Seafood")
    elif x==5:
      data=("Vegetables A-E")
    elif x==6:
      data=("Vegetables F-P ")
    elif x==7:
      data=("Vegetables R-Z")
    elif x==8:
      data=("Fruits A-F")
    elif x==9:
      data=(" Fruits G-P")
    elif x==10:
      data=("Fruits R-Z")
    elif x==11:
      data=("Breads, cereals, fastfood,grains")
    elif x==12:
      data=("Soups")
    elif x==13:
      data=("Desserts, sweets")
    elif x==14:
      data=("Jams, Jellies")
    elif x==15:
      data=("Seeds and Nuts")
    elif x==16:
      data=("Drinks,Alcohol, Beverages")
    
    return render_template("result.html",prediction_text="food category is {}".format(data))

if __name__=="__main__":
    app.run(port=8000)