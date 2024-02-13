import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("linear_salary_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Hello everyone"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(YearsExperience 
                              ):
   
    prediction=classifier.predict([[YearsExperience]])
    print(prediction)
    return prediction



def main():
    st.title("Salary Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Salary ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Years_Experienece = st.text_input("YearsExperience","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(Years_Experienece ))
                                          
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("This is about salary prediction")

if __name__=='__main__':
    main()
    
    
    