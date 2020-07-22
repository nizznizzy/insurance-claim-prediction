from flask import Flask, render_template
from flask import request
import pickle
import numpy as np
import sklearn


app = Flask(__name__)
model = pickle.load(open('random_clf.pkl','rb'))
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=="POST":
        Age = int(request.form['Age'])
        Gender = request.form['Gender']
        Bmi = float(request.form['Bmi'])
        Number_of_children = int(request.form['Num_of_children'])
        Smoker = int(request.form['Smoking'])
        Region = request.form['Region']
        Charges = float(request.form['charges']) 
        prediction = model.predict([[Age,Gender,Bmi,Number_of_children,Smoker,Region,Charges ]])
        output = round(prediction[0],2)
        if output == 0:
            return render_template('index.html', pred_text = "You cannot claim insurance money")
        else:
            return render_template('index.html', pred_text = "You can claim insurance money")


if __name__=="__main__":
    app.run(debug=True)