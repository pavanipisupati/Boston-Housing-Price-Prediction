from flask import Flask, jsonify, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib



app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    model = joblib.load('model/boston_model.pkl')
    df = pd.DataFrame(json, index=[0])

    scaler = StandardScaler()
    scaler.fit(df)

    df_scaled = scaler.transform(df)
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
    y_predict = model.predict(df_scaled)
    

    result = {"Predicted house price: " : y_predict[0]}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)  