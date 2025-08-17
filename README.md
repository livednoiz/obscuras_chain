# 🌌 Obscuras Chain

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![ETH-EVM](https://img.shields.io/badge/ETH-EVM-Blockchain-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-BETA-0.2.0-blue.svg)
<img src="https://github.com/livednoiz/obscuras_chain/blob/main/assets/obs_chain.png" alt="OBS-Chain Logo" width="50%"/>
</div>


**Die dezentrale EVM-Blockchain für eine bessere Welt.**

Obscuras Chain ist ein schlanker, prototypischer Ethereum Virtual Machine (EVM) Node, der es Entwicklern ermöglicht, **Smart Contracts zu deployen, auszuführen und zu testen**, während er das Fundament für eine **dezentrale Organisation (DAO)** legt.

---

## 🎯 Vision & Mission
- Aufbau einer **dezentrale Organisation** zur Förderung einer gerechteren Welt.
- Bereitstellung einer **transparenten, sicheren und offenen Blockchain** für Smart Contracts.
- Förderung von **Community-Driven Entwicklung**, offene Mitgestaltung und Beteiligung.

---

## 🚀 Features

### 🔹 Core EVM Engine
- Stack-basierte Berechnung (OpCodes: `PUSH`, `ADD`, `SUB`, `MUL`, `DIV`, `STORE`, `LOAD`)  
- Eigenes Contract Storage  
- Gas-Mechanik zur Simulation von Ressourcenverbrauch  
- Fehlerbehandlung (Stack-Underflow, Out-of-Gas)

### 🔹 Smart Contract Management
- Deployment mit eindeutiger Adresse  
- Separates Storage pro Contract  
- Call-Funktion für Contract Execution  
- Logging- & Debugging-Funktionalität

### 🔹 Blockchain-Kern
- Blockstruktur mit Hashing (SHA3 / Keccak256)  
- Chain-Verkettung für Konsistenz  
- Optionaler Proof-of-Authority (PoA) Konsens für mehrere Nodes

### 🔹 Developer Friendly
- Minimaler Python-Prototyp  
- Erweiterbar mit neuen OpCodes  
- Lokales Testnetz für einfache Smart Contract Tests

---

## 🛠️ Installation & Nutzung

1. **Python Umgebung vorbereiten**
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```
2. **Abhängigkeiten installieren**
```bash
pip install pysha3 eth-utils eth-keys rlp web3
```
3. **Mini-EVM ausführen**
```bash
python mini_evm_contract.py
```
4. **Smart Contracts deployen & ausführen**
* Deployment über evm.deploy_contract(bytecode)

* Call über evm.call_contract(address)

* Zugriff auf Contract Storage: evm.contracts[address].storage

---

### 🌟 Next Steps
 
1. Implementierung von mehr OpCodes (MOD, EQ, LT, GT, AND, OR)

2. Aufbau einer Server-Schnittstelle (JSON-RPC) für externe Zugriffe

3. Erweiterung zu mehreren Nodes für verteiltes Testnetz

4. Integration von Event Logging und Contract Interaktionen

5. DAO-Mechaniken simulieren und Governance-Struktur testen

---

### 💡 Mitmachen
* Contribute: Forke das Repo und erstelle Pull Requests

* Report Issues: Fehler oder Vorschläge direkt über GitHub Issues

* Community: Diskutiere Ideen für OpCodes, Contracts und Governance

---

🌌 Obscuras Chain – Deine Plattform für dezentrale Entwicklung und bessere Welt.
