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
    logging.info(type(source))
    try:
        abi = compiler.mk_full_signature(source)
        abi_code = 200
    except:
        abi = "Could not be created"
        abi_code = 500
    try:
        json_abi = json.dumps(compiler.mk_full_signature(source))
        json_abi_code = 200
    except:
        json_abi = "Could not be created"
        json_abi_code = 500
    try:
        bytecode = '0x' + compiler.compile(source).hex()
        bytecode_code = 200
    except:
        bytecode = "Could not be created"
        bytecode_code = 500
    try:
        ir = "test"#optimizer.optimize(parse_to_lll(source))
        ir_code = 200
    except:
        ir = "Could not be created"
        ir_code = 500
    
    r_dict = { 'result': {
        'abi': abi,
        'abi_code': abi_code,
        'json': json_abi,
        'json_code': json_abi_code, 
        'bytecode': bytecode,
        'bytecode_code': bytecode_code }
    }
    return make_response(jsonify(r_dict), 200)


if __name__ == '__main__':
    
    app.run(debug=True)
