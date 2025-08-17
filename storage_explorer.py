# storage_explorer.py
import requests

API_URL = "http://127.0.0.1:8545"

# Beispiel: Liste von Contract-Adressen
addresses = [
    # Hier Adressen eintragen, z.B. aus Batch-Deployment
]

for address in addresses:
    resp = requests.get(f"{API_URL}/get_storage", params={"address": address})
    if resp.status_code == 200:
        storage = resp.json()["storage"]
        print(f"Storage for {address}: {storage}")
    else:
        print(f"Error for {address}: {resp.text}")
