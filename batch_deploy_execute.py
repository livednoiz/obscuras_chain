# batch_deploy_execute.py
import requests

API_URL = "http://127.0.0.1:8545"

contracts = [
    [["PUSH", 2], ["PUSH", 3], ["MUL", None], ["STORE", "mul_result"]],
    [["PUSH", 10], ["PUSH", 4], ["DIV", None], ["STORE", "div_result"]],
    [["PUSH", 7], ["PUSH", 3], ["MOD", None], ["STORE", "mod_result"]],
]

addresses = []
for bytecode in contracts:
    resp = requests.post(f"{API_URL}/deploy_contract", json={"bytecode": bytecode, "gas_limit": 100})
    resp.raise_for_status()
    address = resp.json()["address"]
    addresses.append(address)
    print(f"Deployed contract at: {address}")

for address in addresses:
    resp = requests.post(f"{API_URL}/call_contract", json={"address": address})
    resp.raise_for_status()
    storage = resp.json()["storage"]
    print(f"Storage for {address}: {storage}")
