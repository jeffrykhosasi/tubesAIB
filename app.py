import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
import lightgbm

# Load model
model = pickle.load(open('lgb_model.pkl', 'rb'))

# App
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)