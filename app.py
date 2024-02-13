import numpy as np
import pickle
import pandas as pd
from flask import Flask, request


app=Flask(__name__)
pickle_in=open("linear_salary_model.pkl","rb")
classifier=pickle.load(pickle_in)
@app.route("/")
def welcome():
    return "hello everyone"

@app.route("/predict",methods=["Get"])
def predict_note_authentication():
    input_cols=["YearsExperience"]
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))
    prediction=classifier.predict([list1])
    print(prediction)
    return "Hello The answer is"+str(prediction)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)