from flask import Flask, jsonify, request
from flask_api import status
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
import json
import jsonschema
from jsonschema import validate

''' The server app handles all the input requests, 
validates the JSON schema, 
runs the input data through the model picke file and 
returns the predicted house price as JSON response'''

app = Flask(__name__)


'''Function to validate the incoming JSON format against the recommended JSON schema '''
def validateJson(jsonData):
    try:
        with open('app/input_schema.json') as schema_file:
            schema=json.load(schema_file)
            validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


'''Entry point for all the incoming POST requests
and returns the JSON response '''
@app.route("/predict", methods=['POST'])
def handle_post():
    input_json = request.get_json()
    error_message=None

    if input_json == None:
        error_message= "Missing request body"
    elif validateJson(input_json)  == False:
        error_message= "Incoming json format is invalid"
    if error_message!=None:
        return error_message, status.HTTP_400_BAD_REQUEST

    result=do_prediction(input_json)
    return jsonify(message="The predicted house price:",price=result)


''' Function that takes the input data and return the predicted price '''
def do_prediction(input_json):
    model = joblib.load('model/boston_model.pkl')
    df = pd.DataFrame(input_json, index=[0])
    scaler = MinMaxScaler(feature_range=(0, 1))  
    df[['ZN','AGE','TAX','B','LSTAT']] = scaler.fit_transform(df[['ZN','AGE','TAX','B','LSTAT']])
    df_new = pd.DataFrame(df, columns=df.columns)
    y_predict = model.predict(df_new)
    print("The prediction is: ",y_predict)
    result = y_predict[0]
    return result



if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)  