

from flask import Flask, render_template, request
import pandas as pd
#import sklearn
import pickle

model = pickle.load(open("weh_rf.pkl", "rb"))

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('weh_template.html')

@app.route('/predict', methods = ["GET", "POST"])

def Predict():
    if request.method == "POST":
        #Date of Journey
        # Departure DMY
        date_dep = request.form["Date"]
        month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        year = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").year)
        #InDirekt = 1
        print(year,month)
        
        # Source
        Salespartner = request.form["Salespartner"]
        if (Salespartner == 'InDirect'):
            InDirekt = 1
        else:
            InDirekt = 0
        print(InDirekt)


        
        
        # Total_Stops
        
        
        prediction=model.predict([[
            year,
            month,
            InDirekt
        ]])
        
        output=round(prediction[0],2)
        print(output)

        
        return render_template('weh_template.html',prediction_text = "Montly turnover is {}".format(output)) 
    
    return render_template('weh_template.html')
    

if __name__ == '__main__':
    app.run()