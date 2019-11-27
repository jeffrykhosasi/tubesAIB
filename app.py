import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
import lightgbm
import sys

# Load model
model = pickle.load(open('lgbmc_model.sav', 'rb'))

# App
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def predict():

    # get data from form
    # ----
    # needed data is based on the model. the current lgbmc_model.sav used has 3 features: is_4G, n_ad_seen, app_code_count_n, 
    # thus we ask user to input these 3 attributes and take it from the form.
    # ----
    # there is a need to explicitly change the type of the object to create a proper dataframe to be used in the model
    is_4g = int(request.form['is_4g'])
    app_code_count_n = int(request.form['app_code_count_n'])
    n_ad_seen = int(request.form['n_ad_seen'])

    # prepare data as a dataframe for input
    data = [[is_4g, n_ad_seen, app_code_count_n]]
    data = pd.DataFrame(data, columns = ['is_4G','n_ad_seen','app_code_count_n'])

    # predict
    result = model.predict_proba(data)[:,1]

    # return prediction result
    return jsonify({'result': result.tolist()}) 

if __name__ == '__main__':
    app.run(port=5000, debug=False)