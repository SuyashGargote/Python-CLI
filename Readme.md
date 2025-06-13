# 🔐 Password Vault – Secure CLI Password Manager (Python)

A secure command-line password manager built in Python. It uses **Fernet symmetric encryption** from the `cryptography` library to store and retrieve passwords safely. Users must enter a **master password** to access the vault.

> ✅ Perfect for beginners in **Python** and **Cybersecurity** looking to demonstrate real-world encryption, authentication, and file handling skills.

---

## 🚀 Features

- 🔑 Master password protection
- 🔐 Password encryption using `Fernet` (AES-based symmetric encryption)
- 💾 Encrypted password storage in a local JSON file
- 🧩 Modular Python design (separate files for encryption, data handling, and CLI)
- 🧠 Beginner-friendly CLI with secure password input using `getpass`

---

## 📁 Project Structure

password_vault/
├── vault.py # Main CLI interface
├── encryption.py # Fernet key generation + encrypt/decrypt
├── data_handler.py # Load/save JSON vault data
├── auth.py # Master password verification
├── key.key # Auto-generated encryption key (do not share!)
├── vault_data.json # Auto-generated encrypted password storage
└── README.md # This file


---

## 💻 Getting Started

### 🔧 Prerequisites

- Python 3.7 or higher
- `cryptography` package

```bash
pip install cryptography

▶️ Running the Program

```bash
python vault.py

python vault.py
On first run:

Generates an encryption key (key.key)

Creates an empty password vault file (vault_data.json)

🛡️ Security Details
All stored passwords are encrypted using Fernet symmetric encryption (based on AES).

Access is restricted using a master password entered via getpass for terminal safety.

Key file and password vault are excluded from Git tracking via .gitignore.

🧪 Sample Use (CLI Flow)

--- Password Vault ---
1. Add new password
2. Get existing password
3. Exit

Enter choice: 1
Account name: GitHub
Password: *********

Password for GitHub added.

🧠 What I Learned
Symmetric encryption (Fernet)

Secure password handling via Python CLI

JSON-based persistent storage

Writing clean, modular Python scripts

Applying cybersecurity principles as a beginner