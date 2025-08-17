
from flask import Flask, request, jsonify
from mini_evm_contract import MiniEVM

app = Flask(__name__)
evms = {}
OBS_TOKEN_ADDRESS = None

def get_evm():
    global evms, OBS_TOKEN_ADDRESS
    if not evms:
        evm = MiniEVM(gas_limit=1000)
        # OBS-Token-Contract deployen
        obs_token_bytecode = [
            ("PUSH", "creator"),
            ("PUSH", 1000000),
            ("STORE", "balance"),
        ]
        OBS_TOKEN_ADDRESS = evm.deploy_contract(obs_token_bytecode)
        evm.call_contract(OBS_TOKEN_ADDRESS)
        evms[OBS_TOKEN_ADDRESS] = evm
    return evms[OBS_TOKEN_ADDRESS]

@app.route('/obs_transfer', methods=['POST'])
def obs_transfer():
    data = request.get_json()
    sender = data.get('sender')
    receiver = data.get('receiver')
    amount = data.get('amount')
    evm = get_evm()
    contract = evm.contracts[OBS_TOKEN_ADDRESS]
    # Transfer-Logik
    sender_balance = contract.storage.get('balance', 0)
    if sender_balance < amount:
        return jsonify({'error': 'Insufficient balance'}), 400
    contract.storage['balance'] = sender_balance - amount
    receiver_key = f'{receiver}_balance'
    contract.storage[receiver_key] = contract.storage.get(receiver_key, 0) + amount
    return jsonify({'sender_balance': contract.storage['balance'], 'receiver_balance': contract.storage[receiver_key]})

@app.route('/obs_balance', methods=['GET'])
def obs_balance():
    account = request.args.get('account')
    evm = get_evm()
    contract = evm.contracts[OBS_TOKEN_ADDRESS]
    if account == 'creator':
        balance = contract.storage.get('balance', 0)
    else:
        balance = contract.storage.get(f'{account}_balance', 0)
    return jsonify({'account': account, 'balance': balance})

@app.route('/deploy_contract', methods=['POST'])
def deploy_contract():
    data = request.get_json()
    bytecode = data.get('bytecode')
    gas_limit = data.get('gas_limit', 100)
    evm = MiniEVM(gas_limit=gas_limit)
    address = evm.deploy_contract(bytecode)
    evms[address] = evm
    return jsonify({'address': address})

@app.route('/call_contract', methods=['POST'])
def call_contract():
    data = request.get_json()
    address = data.get('address')
    if address not in evms:
        return jsonify({'error': 'Contract not found'}), 404
    evm = evms[address]
    try:
        evm.call_contract(address)
        return jsonify({'storage': evm.contracts[address].storage})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_storage', methods=['GET'])
def get_storage():
    address = request.args.get('address')
    if address not in evms:
        return jsonify({'error': 'Contract not found'}), 404
    evm = evms[address]
    return jsonify({'storage': evm.contracts[address].storage})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8545)
