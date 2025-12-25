# Internal Network Reconnaissance Script

A lightweight Python-based **internal network reconnaissance tool** that gathers key system and network information from a host.  
This script is designed for **offensive security labs, red-team reconnaissance, and cyber security internships**.

---

## 🔍 Overview

This script performs **early-stage internal reconnaissance** by collecting:

- Hostname and IP address
- Private network classification
- Default gateway information
- Configured DNS servers
- Common open local services on `localhost`

It helps attackers or red-teamers **understand the internal network environment** before moving to lateral movement or exploitation phases.

---

## ⚙️ Features

- Detects the system hostname and local IP address
- Identifies whether the IP belongs to a private/internal network range
- Extracts the default gateway (Windows & Linux supported)
- Retrieves configured DNS servers
- Scans for commonly open local services on `127.0.0.1`
- Cross-platform support (Windows & Linux)

---

## 🛠️ Technologies Used

- **Python 3**
- `socket` – Network and port checks
- `subprocess` – System command execution
- `platform` – OS detection
- `re` – Pattern matching for IP parsing

---

## 📌 Reconnaissance Workflow
```
Host Identification
       ↓
Internal IP Validation
       ↓
Gateway Discovery
       ↓
DNS Enumeration
       ↓
Local Service Enumeration
```
---

## ▶️ Usage

Run the script directly:

```bash
python3 network_recon.py
