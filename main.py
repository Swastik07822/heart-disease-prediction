from flask import Flask, request, jsonify, render_template_string,render_template
#from pyngrok import ngrok
from joblib import load
import numpy as np



app = Flask(__name__)

def predict_heart_disease(data):
    
    model = load('./model')
 
    ans = model.predict(data)

    return ans

@app.route('/')
def home():

    return render_template('form.html')


@app.route('/predict', methods=['POST'])
def predict():
    
    age = request.form['age']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs=request.form['fbs']
    restecg = request.form['restecg']
    thalach= request.form['thalach']
    exang  = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca=request.form['ca']
    thal = request.form['thal']

    data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    
    data  = np.array([data],dtype=float)

    prediction = predict_heart_disease(data)
    
    ans = ''
    
    context  ={}
    
    if prediction:
        
        ans = 'At Risk'
        
        context = {'ans':ans}
        
    else:
        
        ans = 'Out of Danger'
        
        context ={'ans':ans}

    return render_template('result.html',**context)


# Run Flask app

app.run(debug=True)