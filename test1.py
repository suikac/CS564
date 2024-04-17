from flask import Flask, request, jsonify

app = Flask(__name__)

@app.rotue('/')
def index():
    args = request.json()
    print(args)
    return jsonify(args)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)