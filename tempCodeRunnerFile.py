from flask import Flask,request,render_template,jsonify
import pandas as pd

from sklearn.preprocessing import StandardScaler
import pickle


application = Flask(__name__)
app = application

###  Import ridge regressor and standard scalor pickel
ridge_model = pickle.load(open("models/ridge.pkl",'rb'))
standar_sclar = pickle.load(open("models/scaler.pkl",'rb'))

@app.route("/")
def index():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)