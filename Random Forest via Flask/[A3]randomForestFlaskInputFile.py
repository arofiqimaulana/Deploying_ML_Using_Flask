import pickle
from flask import Flask, request
import numpy as np 
import pandas as pd

with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict')
def predict():
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_height = request.args.get('p_height')
    p_width = request.args.get('p_width')

    prediction = model.predict(np.array([[s_length, s_width, p_height, p_width]]))

    return str(prediction)

@app.route('/predict_file',methods=['POST'])
def predict_file():
    input_data = pd.read_csv(request.files.get('file'),sep=';',header=None)
    prediction = model.predict(np.array(input_data))

    return str(list(prediction))

if __name__ == '__main__':
    app.run(debug=True,port=3000)

# cara run di postman : http://127.0.0.1:3000/predict_file kemudian import file csv di bagian body -> form-data ubah text ke file