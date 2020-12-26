from flask import Flask, request, jsonify, render_template
import os
import numpy as np
import json
import pickle



#Getting saved artifacts 
__data_columns = None
__prop_area= None
__dependents= None
__model= None

#Getting prediction
def get_prediction(gender, married, education, credit_history, dependents, property_area):
    load_saved_artifacts()
    dep= 'dependents_' + dependents
    prop= 'property_area_' + property_area
    try:
        dep_index= __data_columns.index(dep.lower())
        prop_index= __data_columns.index(prop.lower())
    except:
        dep_index= -1
        prop_index= -1
    
    x = np.zeros(len(__data_columns))

    if gender == "Male":
        x[0]= 1
    else:
        x[0] = 0     
    
    if married == "Married":
        x[1]= 1
    else:
        x[1] = 0
    
    if gender == "Graduate":
        x[2]= 1
    else:
        x[2] = 0
    
    if credit_history == "All debts paid":
        x[3]= 1
    else:
        x[3] = 0
    
    if dep_index>=0:
        x[dep_index]= 1
    if prop_index >=0:
        x[prop_index]= 1
    
    if __model.predict([x])[0] == 0:
        return "Oops!! Your application was rejected."
    else:
        return "Congratulations!!! Your application is approved."

#Loading saved artifacts
def load_saved_artifacts():
    global __prop_area
    global __dependents
    global __data_columns
    global __model

    with open("./artifacts/columns.json", "r") as f:
        __data_columns= json.load(f)['data_columns']
        __prop_area= __data_columns[8:]
        __prop_area= [i.split('_')[2] for i in __prop_area]
        __dependents= __data_columns[4:8]
        __dependents= [i.split('_')[1] for i in __dependents]
    
    with open('./artifacts/loan_predictor.pickle', 'rb') as f:
        __model = pickle.load(f)


#Running flask 

app= Flask(__name__)


#home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])
def predict():
    gender= request.form['gender']
    married= request.form['married']
    education= request.form['education']
    cred_hist= request.form['cred_hist']
    dependencies= request.form['dependencies']
    prop_area= request.form['property_area']

    prediction=  get_prediction(gender, married, education, cred_hist, dependencies, prop_area)
    return render_template('index.html', output=prediction)


if __name__ ==  "__main__":
    load_saved_artifacts()
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)