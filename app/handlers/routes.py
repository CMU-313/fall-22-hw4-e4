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


    @app.route('/predict_on_health')
    def predict_health():
        # use entries from the query string here but could also use json
        # implictly, convert to int 0, sp raise 400
        age = int(request.args.get('age'))
        absences = int(request.args.get('absences'))
        health = int(request.args.get('health'))
        # check the range for age, absences, health here
        if (not (age >= 15 and age <= 22)):
            return "Invalid Request Field", 400
        if (not (absences >= 0 and absences <= 93)):
            return "Invalid Request Field", 400
        if (not (health >= 1 and health <= 5)):
            return "Invalid Request Field", 400
        query_df = pd.DataFrame({
            'age': pd.Series(age),
            'health': pd.Series(health),
            'absences': pd.Series(absences)
        })
        # don't use pd.get_dummies
        prediction = clf.predict(query_df)
        return jsonify(np.ndarray.item(prediction))

    @app.route('/predict_on_study')
    def predict_study():
        #use entries from the query string here but could also use json
        studytime = int(request.args.get('studytime'))
        absences = int(request.args.get('absences'))
        failures = int(request.args.get('failures'))
        if (not (studytime >= 1 and studytime <= 4)):
            return "Invalid Request Field", 400
        if (not (absences >= 0 and absences <= 93)):
            return "Invalid Request Field", 400
        if (not (failures >= 1 and failures <= 4)):
            return "Invalid Request Field", 400
        query_df = pd.DataFrame({
            'studytime': pd.Series(studytime),
            'failures': pd.Series(failures),
            'absences': pd.Series(absences)
        })
        prediction = clf.predict(query_df)
        return jsonify(np.ndarray.item(prediction))
