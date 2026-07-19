# ⛓️ Mini Blockchain

This project demonstrates the fundamental concepts behind blockchain technology, including cryptographic hashing, block linking, Proof of Work (mining), and blockchain validation.

---

## 📌 Project Overview

The goal of this project is to understand how a blockchain maintains data integrity without relying on a central authority.

The blockchain consists of:

- A `Block` class to represent individual blocks.
- A `Blockchain` class to manage the chain.
- SHA-256 hashing for secure block identification.
- Proof of Work mining using a nonce.
- Chain validation to detect tampering.

---

## 🚀 Features

- ✅ Genesis Block creation
- ✅ SHA-256 Cryptographic Hashing
- ✅ Block Linking using Previous Hash
- ✅ Proof of Work (Mining)
- ✅ Nonce Generation
- ✅ Blockchain Validation
- ✅ Tampering Detection

---

## 🛠 Technologies Used

- Python 3
- hashlib
- datetime
- Git
- GitHub

---

## 📂 Project Structure

```
Mini-Blockchain/
│
├── block.py
├── blockchain.py
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│
└── screenshots/
```

---

## ⚙️ How It Works

### Step 1

Create the Genesis Block.

↓

### Step 2

Add a new block containing transaction data.

↓

### Step 3

Generate a SHA-256 hash.

↓

### Step 4

Mine the block using Proof of Work by incrementing the nonce until the hash satisfies the target difficulty.

↓

### Step 5

Link the block to the previous block using its hash.

↓

### Step 6

Validate the blockchain by verifying:

- Current block hash
- Previous hash linkage

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/LokeshO-O/Mini-Blockchain.git
```

Go inside the project:

```bash
cd Mini-Blockchain
```

Run:

```bash
python main.py
```

---

## 💻 Sample Output

```
--------------------------------------------------
Index: 0
Payload: Genesis Block
Nonce: 18452
Previous Hash: 0000
Hash: 0000a2...

--------------------------------------------------
Index: 1
Payload: Lokesh pays Mansi ₹100
Nonce: 75291
Previous Hash: 0000a2...
Hash: 0000bc...

--------------------------------------------------
Blockchain Valid: True
```

---

## 📚 Concepts Learned

During this project, I learned:

- Blockchain Architecture
- SHA-256 Hashing
- Immutable Data Structures
- Proof of Work (Mining)
- Nonce Generation
- Blockchain Validation
- Tampering Detection
- Object-Oriented Programming in Python

---

## 🔮 Future Improvements

- Transaction Pool
- Wallet System
- Digital Signatures
- Peer-to-Peer Networking
- Smart Contracts
- REST API
- Adjustable Mining Difficulty

---

## 👨‍💻 Author

**Lokesh**

