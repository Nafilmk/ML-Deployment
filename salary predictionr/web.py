from flask import Flask,render_template,request
import pickle
import numpy as np


app=Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def salary():
    return render_template("salary.html")


@app.route("/predict",methods=["POST"])
def predict():
    experience=float(request.values["experience"])
    experience=np.reshape(experience,(-1,1))
    output=model.predict(experience)
    output=output.item()
    output=round(output,2)
    print(output)
    return render_template("result.html",prediction_text="salary per month ${}".format(output))

if __name__=="__main__":
    app.run(port=8088)