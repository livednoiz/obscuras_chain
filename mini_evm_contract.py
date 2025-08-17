# mini_evm_contract.py
# Minimal EVM mit Contract Deployment & Call

import hashlib
import uuid

def keccak256(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()

# --- Stack ---
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise Exception("Stack underflow")
        return self.items.pop()

    def __repr__(self):
        return str(self.items)

# --- Contract ---
class Contract:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.storage = {}

# --- Mini EVM ---
class MiniEVM:
    OPCODE_GAS = {
        "PUSH": 1, "ADD": 3, "SUB": 3, "MUL": 5, "DIV": 5,
        "MOD": 5, "EQ": 2, "LT": 2, "GT": 2, "AND": 2, "OR": 2,
        "STORE": 20, "LOAD": 10, "PRINT": 0
    }

    def __init__(self, gas_limit=100):
        self.stack = Stack()
        self.contracts = {}  # deployed contracts
        self.gas = gas_limit

    def consume_gas(self, op):
        cost = self.OPCODE_GAS.get(op, 0)
        if self.gas < cost:
            raise Exception(f"Out of gas for {op} (needed {cost}, remaining {self.gas})")
        self.gas -= cost

    # --- Deploy contract ---
    def deploy_contract(self, bytecode):
        address = str(uuid.uuid4())[:8]  # einfache zufällige Adresse
        self.contracts[address] = Contract(bytecode)
        print(f"Contract deployed at {address}")
        return address

    # --- Call contract ---
    def call_contract(self, address):
        if address not in self.contracts:
            raise Exception("Contract not found")
        contract = self.contracts[address]
        self.execute(contract.bytecode, contract.storage)

    # --- Execute bytecode ---
    def execute(self, bytecode, storage=None):
        pc = 0
        if storage is None:
            storage = {}
        stack = self.stack
        while pc < len(bytecode):
            op, arg = bytecode[pc]
            self.consume_gas(op)

            if op == "PUSH":
                stack.push(arg)
            elif op == "ADD":
                b = stack.pop()
                a = stack.pop()
                stack.push(a + b)
            elif op == "SUB":
                b = stack.pop()
                a = stack.pop()
                stack.push(a - b)
            elif op == "MUL":
                b = stack.pop()
                a = stack.pop()
                stack.push(a * b)
            elif op == "DIV":
                b = stack.pop()
                a = stack.pop()
                stack.push(a // b if b != 0 else 0)
            elif op == "MOD":
                b = stack.pop()
                a = stack.pop()
                stack.push(a % b if b != 0 else 0)
            elif op == "EQ":
                b = stack.pop()
                a = stack.pop()
                stack.push(1 if a == b else 0)
            elif op == "LT":
                b = stack.pop()
                a = stack.pop()
                stack.push(1 if a < b else 0)
            elif op == "GT":
                b = stack.pop()
                a = stack.pop()
                stack.push(1 if a > b else 0)
            elif op == "AND":
                b = stack.pop()
                a = stack.pop()
                stack.push(a & b)
            elif op == "OR":
                b = stack.pop()
                a = stack.pop()
                stack.push(a | b)
            elif op == "STORE":
                key = arg
                value = stack.pop()
                storage[key] = value
            elif op == "LOAD":
                key = arg
                stack.push(storage.get(key, 0))
            elif op == "PRINT":
                print("Stack:", stack)
                print("Storage:", storage)
                print("Gas remaining:", self.gas)
            else:
                raise Exception(f"Unknown opcode {op}")
            pc += 1
        return storage

# --- Beispiel Smart Contract ---

# --- Minimaler OBS-Token-Contract ---
# Initialisiert ein Guthaben für einen Account und ermöglicht einfache Transfers
obs_token_bytecode = [
    # Initialguthaben für 'creator'
    ("PUSH", "creator"),
    ("PUSH", 1000000),
    ("STORE", "balance"),
    # Transfer 100 OBS von 'creator' zu 'alice'
    ("LOAD", "balance"),      # Lade Guthaben von 'creator'
    ("PUSH", 100),
    ("SUB", None),
    ("STORE", "balance"),     # Neues Guthaben für 'creator'
    ("PUSH", "alice"),
    ("PUSH", 100),
    ("STORE", "alice_balance"), # Guthaben für 'alice'
    # Balance-Abfrage für 'alice'
    ("LOAD", "alice_balance"),
    ("PRINT", None)
]

# Beispiel Smart Contract: Berechnet result = (5+3)*2
contract_bytecode = [
    ("PUSH", 5),
    ("PUSH", 3),
    ("ADD", None),
    ("PUSH", 2),
    ("MUL", None),
    ("STORE", "result"),
]

# --- Nutzung: OBS-Token als Standard-Token deployen ---
evm = MiniEVM(gas_limit=1000)
OBS_TOKEN_ADDRESS = evm.deploy_contract(obs_token_bytecode)
print(f"OBS-Token deployed at: {OBS_TOKEN_ADDRESS}")
evm.call_contract(OBS_TOKEN_ADDRESS)
obs_storage = evm.contracts[OBS_TOKEN_ADDRESS].storage
print("OBS-Token Storage:", obs_storage)

# Beispiel Smart Contract
address = evm.deploy_contract(contract_bytecode)
evm.call_contract(address)
contract_storage = evm.contracts[address].storage
print("Contract final storage:", contract_storage)
