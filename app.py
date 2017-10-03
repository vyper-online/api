import json, logging, requests, sys
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import viper
from viper import compiler, optimizer
from viper.parser import parse_to_lll

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)

COMPILE_ENDPOINT = '/compile/'


@app.route(COMPILE_ENDPOINT, methods=['GET', 'POST'])
def compile():
    source = request.form.get('source', '')
    abi = compiler.mk_full_signature(code)
    json_abi = json.dumps(compiler.mk_full_signature(code))
    bytecode = '0x' + compiler.compile(code).hex()
    ir = optimizer.optimize(parse_to_lll(code))
    
    r_dict = { 'result': {
        'msg': 'Compilation successful',
        'abi': abi,
        'json': json_abi,
        'bytecode': bytecode,
        'ir': ir,
        'code': 200, }
    }
    return make_response(jsonify(r_dict), 200)


if __name__ == '__main__':
    
    app.run(debug=True)