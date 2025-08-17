# evm_cli.py
import requests
import json

API_URL = "http://127.0.0.1:8545"

def main():
    while True:
        print("\nMini-EVM CLI")
        print("1. Contract deployen")
        print("2. Contract ausführen")
        print("3. Storage abfragen")
        print("4. Beenden")
        choice = input("Auswahl: ").strip()
        if choice == "1":
            bytecode_str = input("Bytecode als JSON (z.B. [[\"PUSH\", 5], [\"PUSH\", 3], [\"ADD\", null], [\"STORE\", \"result\"]]): ")
            try:
                bytecode = json.loads(bytecode_str)
            except Exception as e:
                print(f"Fehler im Bytecode: {e}")
                continue
            gas_limit = input("Gas-Limit (Standard 100): ").strip()
            gas_limit = int(gas_limit) if gas_limit else 100
            resp = requests.post(f"{API_URL}/deploy_contract", json={"bytecode": bytecode, "gas_limit": gas_limit})
            if resp.status_code == 200:
                address = resp.json()["address"]
                print(f"Contract deployed at: {address}")
            else:
                print(f"Fehler: {resp.text}")
        elif choice == "2":
            address = input("Contract-Adresse: ").strip()
            resp = requests.post(f"{API_URL}/call_contract", json={"address": address})
            if resp.status_code == 200:
                storage = resp.json()["storage"]
                print(f"Contract storage: {storage}")
            else:
                print(f"Fehler: {resp.text}")
        elif choice == "3":
            address = input("Contract-Adresse: ").strip()
            resp = requests.get(f"{API_URL}/get_storage", params={"address": address})
            if resp.status_code == 200:
                storage = resp.json()["storage"]
                print(f"Storage: {storage}")
            else:
                print(f"Fehler: {resp.text}")
        elif choice == "4":
            print("Beende CLI.")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
