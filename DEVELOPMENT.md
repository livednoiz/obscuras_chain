# Entwicklungsdokumentation – Obscuras Chain

## 1. Projektübersicht
Obscuras Chain ist ein minimalistischer, prototypischer Ethereum Virtual Machine (EVM) Node in Python. Ziel ist es, Smart Contracts und einen eigenen Standard-Token (OBS-Coin) bereitzustellen und eine dezentrale Organisation zu simulieren.

## 2. Architektur & Komponenten
- **Mini-EVM**: Stack-basierte virtuelle Maschine mit grundlegenden OpCodes und Contract-Management.
- **OBS-Token**: Standard-Token, der beim Start automatisch deployed wird. Unterstützt Transfers und Balance-Abfragen.
- **JSON-RPC Server**: HTTP-Schnittstelle für Contract-Interaktionen, Token-Transfers und Storage-Abfragen.

## 3. Installation & Start
```bash
# Python-Umgebung vorbereiten
python3 -m venv .venv
source .venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# JSON-RPC Server starten
python3 evm_rpc_server.py
```

## 4. API-Dokumentation
### Contract-Interaktion
- **Deploy Contract**
  - `POST /deploy_contract`
  - Body: `{ "bytecode": [["PUSH", 5], ["PUSH", 3], ["ADD", null], ...], "gas_limit": 100 }`
  - Response: `{ "address": "..." }`

- **Call Contract**
  - `POST /call_contract`
  - Body: `{ "address": "..." }`
  - Response: `{ "storage": {...} }`

- **Get Storage**
  - `GET /get_storage?address=...`
  - Response: `{ "storage": {...} }`

### OBS-Token
- **Transfer**
  - `POST /obs_transfer`
  - Body: `{ "sender": "creator", "receiver": "alice", "amount": 100 }`
  - Response: `{ "sender_balance": ..., "receiver_balance": ... }`

- **Balance-Abfrage**
  - `GET /obs_balance?account=alice`
  - Response: `{ "account": "alice", "balance": ... }`

## 5. Beispiel-Interaktionen
```bash
# Contract deployen
curl -X POST http://127.0.0.1:8545/deploy_contract \
  -H "Content-Type: application/json" \
  -d '{"bytecode": [["PUSH", 5], ["PUSH", 3], ["ADD", null], ["STORE", "result"]], "gas_limit": 100}'

# OBS-Token transferieren
curl -X POST http://127.0.0.1:8545/obs_transfer \
  -H "Content-Type: application/json" \
  -d '{"sender": "creator", "receiver": "alice", "amount": 100}'

# Guthaben abfragen
curl "http://127.0.0.1:8545/obs_balance?account=alice"
```

## 6. Erweiterbarkeit
- Neue OpCodes können in `MiniEVM.OPCODE_GAS` und der `execute`-Methode ergänzt werden.
- Weitere Endpunkte lassen sich im JSON-RPC Server hinzufügen.
- Smart Contracts können beliebig gestaltet und getestet werden.

## 7. Testen
- Einzelne OpCodes: `test_evm_opcodes.py`
- Batch-Deployment: `batch_deploy_execute.py`
- Storage-Explorer: `storage_explorer.py`
- Event-Logger: `event_logger.py`
- Interaktives CLI: `evm_cli.py`

## 8. Community & Beiträge
- Forken Sie das Repository und erstellen Sie Pull Requests.
- Melden Sie Fehler oder Feature-Wünsche über GitHub Issues.
- Diskutieren Sie neue Ideen und Governance-Mechanismen.

---
Obscuras Chain – Ihre Plattform für dezentrale Entwicklung und den OBS-Coin.
