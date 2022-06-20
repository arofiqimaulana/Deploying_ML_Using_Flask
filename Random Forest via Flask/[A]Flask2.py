from flask import Flask, request

app = Flask(__name__)

# nama root yang akan diakses misal / atau /about atau /home
@app.route('/',methods=['POST'])

def add():
    a = request.form['a']
    b = request.form['b']

    return str(int(a) + int(b))

if __name__ == '__main__':
    app.run(debug=True,port=6000)

# cara run di postman : http://127.0.0.1:6000/ 
# kemudian mengisikan parameter a dan b di form-data