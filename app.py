import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
# Initilaize the Flask application
app = Flask(__name__)
# Home Route
@app.route('/') 
def home():
    return render_template('tree.html')
# Prediction Function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 6)
    loaded_model = pickle.load(open("dt.pickle", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result) == 1:
            prediction = "The applicant most likely to Default"
        else:
            prediction = "The applicant is not likely to Default"
    return render_template("tree.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    