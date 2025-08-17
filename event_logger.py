# event_logger.py
import requests
import json
from datetime import datetime

API_URL = "http://127.0.0.1:8545"
LOG_FILE = "evm_events.log"

def log_event(event_type, details):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "details": details
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

# Beispiel: Contract deployen und ausführen mit Logging
contract_bytecode = [["PUSH", 2], ["PUSH", 3], ["MUL", None], ["STORE", "mul_result"]]
resp = requests.post(f"{API_URL}/deploy_contract", json={"bytecode": contract_bytecode, "gas_limit": 100})
resp.raise_for_status()
address = resp.json()["address"]
log_event("deploy", {"address": address, "bytecode": contract_bytecode})

resp = requests.post(f"{API_URL}/call_contract", json={"address": address})
resp.raise_for_status()
storage = resp.json()["storage"]
log_event("call", {"address": address, "storage": storage})

print(f"Events wurden in {LOG_FILE} protokolliert.")
