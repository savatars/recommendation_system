
from flask import Flask,jsonify,render_template,request
import pickle
import numpy as np 

app=Flask(__name__)
app.secret_key="#####"

#loading the pickled model

#this is just for test purposes
@app.route(“/”)
def hello():
 return “Hello World!”

 if __name__ == “__main__”:
 app.run()