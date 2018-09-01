from flask import Flask, request, jsonify
app = Flask(__name__)

def coba():
    json = request.get_json()
    return jsonify(json)

@app.route('/', methods=["GET"])
def json():
    json = request.get_json()
    return "get ok"
    
@app.route('/json', methods=["POST"])
def hello():
    return coba()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')