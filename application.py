from flask import Flask,request,render_template,jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle


application = Flask(__name__)
app = application

@app.route("/")
def index():
    return "HELLO now you are the guest of the house"

if __name__=='__main__':
    app.run(debug=True)