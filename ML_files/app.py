import pandas as pd
from flask import Flask, jsonify, request
import pickle
from lightfm import LightFM
import scipy.sparse as sp
from scipy.sparse import vstack
import pickle
import numpy as np
import pandas as pd
import random
from scipy.sparse import csr_matrix

class recommender:
    def __init__(self,file_model,item_prop,n_items):
        self.n_items=n_items
        self.file_model=file_model
        self.item_prop=item_prop
        store_model=open(self.file_model,'rb')
        store_item_prop=open(self.item_prop,'rb')
        self.model=pickle.load(store_model)
        self.item_to_property_matrix_sparse=pickle.load(store_item_prop)
    def get_predictions(self,user_id):
        pid_array = np.arange(self.n_items, dtype=np.int32)
        predictions = self.model.predict(user_id,pid_array,item_features=self.item_to_property_matrix_sparse,num_threads=4)
        return predictions 

r=recommender('model.pickle','item_to_property_matrix_sparse.pickle',88000)
model=open('model.pickle','rb')        


# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    data = request.get_json(force=True)
    print(data)
    result=r.get_predictions(data['input'])
    output = {'results': list(result)}
    return output

if __name__ == '__main__':
    app.run(port = 5000, debug=True)