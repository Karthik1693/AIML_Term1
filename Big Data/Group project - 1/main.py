from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('heart_disease_prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('page.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        
        input1 = float(request.form['fname1'])
        input2 = float(request.form['fname2']) 
        input3 = float(request.form['fname3'])
        input4 = float(request.form['fname4'])
        input5 = float(request.form['fname5'])
        input6 = float(request.form['fname6'])
        input7 = float(request.form['fname7'])
        input8 = float(request.form['fname8'])
        input9 = float(request.form['fname9'])
        input10 = float(request.form['fname10'])
        input11 = float(request.form['fname11'])
        input12 = float(request.form['fname12'])
        input13 = float(request.form['fname13'])
      
       
        prediction=model.predict([[input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13]])
        
        if int(prediction) == 0:
            result = "You do not have a heart disease"
        else:
            result = "You have a heart disease"
            
        return render_template('page.html',prediction_texts=result)
        #output=round(prediction[0],2)

if __name__=="__main__":
    app.run(debug=True)