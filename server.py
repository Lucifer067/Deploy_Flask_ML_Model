from flask import Flask, request, jsonify, render_template
import utils
import os

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

    prediction=  utils.get_prediction(gender, married, education, cred_hist, dependencies, prop_area)
    return render_template('index.html', output=prediction)


if __name__ ==  "__main__":
    port= int(os.environ.get('PORT', 5000))
    utils.load_saved_artifacts()
    app.run(port= port, debug= True, use_reloader= False)