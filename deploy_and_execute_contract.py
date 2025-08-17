# deploy_and_execute_contract.py
import requests
import json

API_URL = "http://127.0.0.1:8545"

# Beispiel-Bytecode: result = (5 + 3) * 2
contract_bytecode = [
    ["PUSH", 5],
    ["PUSH", 3],
    ["ADD", None],
    ["PUSH", 2],
    ["MUL", None],
    ["STORE", "result"]
]

def deploy_contract(bytecode, gas_limit=100):
    resp = requests.post(f"{API_URL}/deploy_contract", json={"bytecode": bytecode, "gas_limit": gas_limit})
    resp.raise_for_status()
    address = resp.json()["address"]
    print(f"Contract deployed at: {address}")
    return address

def call_contract(address):
    resp = requests.post(f"{API_URL}/call_contract", json={"address": address})
    resp.raise_for_status()
    storage = resp.json()["storage"]
    print(f"Contract storage: {storage}")
    return storage

def main():
    address = deploy_contract(contract_bytecode)
    storage = call_contract(address)

if __name__ == "__main__":
    main()
