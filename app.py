from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='templates')

model_path1 = f'C:\\Users\\91942\\Downloads\\attrition-final\\random_forest.pkl'
model1 = pickle.load(open(model_path1, 'rb'))

model_path2 = f'C:\\Users\\91942\\Downloads\\attrition-final\\random_forest_s2.pkl'
model2 = pickle.load(open(model_path2, 'rb'))

standard_to = StandardScaler()

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", upload=False)

@app.route("/form-1", methods=['GET', 'POST'])
def form1():
    if request.method == 'GET':
        return render_template("form1.html", upload=False)
    
    elif request.method == 'POST':
        Age = int(request.form['Age'])
        Distance_from_home = int(request.form['Distance_from_home'])
        EnvironmentSatisfaction = int(request.form['EnvironmentSatisfaction'])
        JobInvolvement = int(request.form['JobInvolvement'])
        JobLevel = int(request.form['JobLevel'])
        JobRole = int(request.form['JobRole'])
        JobSatisfaction = int(request.form['JobSatisfaction'])
        MaritalStatus = int(request.form['MaritalStatus'])
        MonthlyIncome = int(request.form['MonthlyIncome'])
        OverTime = int(request.form['OverTime'])
        StockOptionLevel = int(request.form['StockOptionLevel'])
        TotalWorkingYears = int(request.form['TotalWorkingYears'])
        YearsAtCompany = int(request.form['YearsAtCompany'])
        YearsInCurrentRole = int(request.form['YearsInCurrentRole'])
        YearsWithCurrManager = int(request.form['YearsWithCurrManager'])
       
        result = model1.predict([[Age, Distance_from_home, EnvironmentSatisfaction, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, OverTime, StockOptionLevel, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsWithCurrManager]])
        
        if(result == 0):
            return render_template('no.html')
        elif(result == 1):
            return render_template('yes.html')
        return render_template('error.html')
        


@app.route("/form-2", methods=['GET', 'POST'])
def form2():
    if request.method == 'GET':
        return render_template("form2.html", upload=False)
    
    elif request.method == 'POST':
        Age = int(request.form['Age'])
        Daily_rate = int(request.form['Daily_rate'])
        Distance_from_home = int(request.form['Distance_from_home'])
        EnvironmentSatisfaction = int(request.form['EnvironmentSatisfaction'])
        hourly_rate = int(request.form['hourly_rate'])
        JobRole = int(request.form['JobRole'])        
        MonthlyIncome = int(request.form['MonthlyIncome'])
        MonthlyRate = int(request.form['MonthlyRate'])
        Num_companies_worked = int(request.form['Num_companies_worked'])
        OverTime = int(request.form['OverTime'])
        Percent_hike = int(request.form['Percent_hike'])
        StockOptionLevel = int(request.form['StockOptionLevel'])
        TotalWorkingYears = int(request.form['TotalWorkingYears'])
        YearsAtCompany = int(request.form['YearsAtCompany'])
        Yearswithmanager= int(request.form['Yearswithmanager'])
        
        

        result = model2.predict([[Age, Daily_rate,Distance_from_home ,EnvironmentSatisfaction ,hourly_rate, JobRole, MonthlyIncome, MonthlyRate,Num_companies_worked ,OverTime ,Percent_hike , StockOptionLevel,  TotalWorkingYears,  YearsAtCompany, Yearswithmanager]])
        
        if(result == 0):
            return render_template('no.html')
        elif(result == 1):
            return render_template('yes.html')
        return render_template('error.html')
        
        
    

if __name__=="__main__":
    app.run(debug=True)