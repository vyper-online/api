import json, requests
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

COMPILE_ENDPOINT = '/compile/'


@app.route(COMPILE_ENDPOINT, methods=['GET',])
def compile():
    q = request.args.get('q', '')
    print(q)
    
    r_dict = { 'result': { 'msg': 'All looks fine', 'code': 200 } }
    return make_response(jsonify(r_dict), 200)


if __name__ == '__main__':
    
    app.run(debug=True)