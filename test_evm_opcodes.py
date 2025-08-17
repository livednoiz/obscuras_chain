# test_evm_opcodes.py
from mini_evm_contract import MiniEVM

test_bytecodes = {
    "MOD": [
        ("PUSH", 10), ("PUSH", 3), ("MOD", None), ("STORE", "mod_result"), ("PRINT", None)
    ],
    "EQ": [
        ("PUSH", 5), ("PUSH", 5), ("EQ", None), ("STORE", "eq_result"), ("PRINT", None)
    ],
    "LT": [
        ("PUSH", 2), ("PUSH", 5), ("LT", None), ("STORE", "lt_result"), ("PRINT", None)
    ],
    "GT": [
        ("PUSH", 7), ("PUSH", 3), ("GT", None), ("STORE", "gt_result"), ("PRINT", None)
    ],
    "AND": [
        ("PUSH", 6), ("PUSH", 3), ("AND", None), ("STORE", "and_result"), ("PRINT", None)
    ],
    "OR": [
        ("PUSH", 4), ("PUSH", 1), ("OR", None), ("STORE", "or_result"), ("PRINT", None)
    ],
}

for name, bytecode in test_bytecodes.items():
    print(f"\n--- Test {name} ---")
    evm_test = MiniEVM(gas_limit=50)
    addr = evm_test.deploy_contract(bytecode)
    evm_test.call_contract(addr)
    print(f"Storage: {evm_test.contracts[addr].storage}")
