import json, logging, os, requests, sys
from flask import abort, Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
import vyper
from vyper import compiler, optimizer
from vyper.parser.parser import parse_to_lll

#sys.path.append(os.path.join(os.path.dirname(__file__), "vyper_semantics"))

#from vyper_semantics.kvyper import krun, vyper2lll, lll2evm
#from vyper_semantics.scripts.vyper_parser import main as parse
#from vyper_semantics.scripts.op2byte import encode as op2byte

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)


@app.route('/<endpoint>/', methods=['GET', 'POST'])
@cross_origin()
def compile(endpoint):
    if endpoint not in ['compile', 'compile-k']:
        abort(500)
    source = request.form.get('source', '')
    try:
        if endpoint == 'compile':
            abi = compiler.mk_full_signature(source)
            abi_code = 200
        else:
            raise Exception('Not available')
    except Exception as e:
        abi = str(e)
        abi_code = 500
    try:
        if endpoint == 'compile':
            json_abi = json.dumps(compiler.mk_full_signature(source))
            json_abi_code = 200
        else:
            raise Exception('Not available')
    except Exception as e:
        json_abi = str(e)
        json_abi_code = 500
    try:
        if endpoint == 'compile':
            bytecode = compiler.compile_code(source)['bytecode']
            bytecode_code = 200
        else:
            raise Exception('Not available')
    except Exception as e:
        bytecode = str(e)
        bytecode_code = 500
    try:
        if endpoint == 'compile':
            ir = optimizer.optimize(parse_to_lll(source))
            ir = str(ir)
            ir_code = 200
        else:
            raise Exception('Not available')
            #ast = parse(source)
            #print("lala")
            #print(ast)          
            #ir = vyper2lll(ast)
            #ir_code = 200
    except Exception as e:
        ir = str(e)
        ir_code = 500
    
    r_dict = { 'result': {
        'abi': abi,
        'abi_code': abi_code,
        'json': json_abi,
        'json_code': json_abi_code, 
        'bytecode': bytecode,
        'bytecode_code': bytecode_code,
        'lll': ir,
        'lll_code': ir_code }
    }
    return make_response(jsonify(r_dict), 200)


if __name__ == '__main__':
    
    app.run(debug=True)
