from flask import Flask, request

app = Flask(__name__)

# nama root yang akan diakses misal / atau /about atau /home
@app.route('/',methods=['GET'])

def add():
    a = request.args.get('a')
    b = request.args.get('b')

    return str(int(a) + int(b))

if __name__ == '__main__':
    app.run(debug=True,port=7000)

# cara run di web : http://127.0.0.1:7000/?a=15&b=10