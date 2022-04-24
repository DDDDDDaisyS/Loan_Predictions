# import the required plugins
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pickle
import pandas as pd
import numpy

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('model.p', 'rb'))

class Predict(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        res = model.predict(df)
        
        return res.tolist() 
    
# assign endpoint
api.add_resource(predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True)