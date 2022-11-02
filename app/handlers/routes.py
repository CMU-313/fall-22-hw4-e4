import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"

    @app.route('/predict_on_study')
    def predict_study():
        #use entries from the query string here but could also use json
        G1 = int(request.args.get('G1'))
        G2 = int(request.args.get('G2'))
        failures = int(request.args.get('failures'))
        if (not (G1 >= 0 and G1 <= 20)):
            return "Invalid Request Field", 400
        if (not (G2 >= 0 and G2 <= 20)):
            return "Invalid Request Field", 400
        if (not (failures >= 1 and failures <= 4)):
            return "Invalid Request Field", 400
        query_df = pd.DataFrame({
            'G1': pd.Series(G1),
            'G2': pd.Series(G2),
            'failures': pd.Series(failures)
        })
        prediction = clf.predict(query_df)
        return jsonify(np.ndarray.item(prediction))
