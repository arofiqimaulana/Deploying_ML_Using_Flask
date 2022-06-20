import pickle
from flask import Flask, request
import numpy as np 

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

if __name__ == '__main__':
    app.run(debug=True,port=3000)

# cara run : http://127.0.0.1:3000/predict?s_length=2&s_width=3&p_height=5&p_width=6