# 🛡️ Cryptography MET CS789 - Team Project Report

---

### Table of Contents
1. [Project Overview](#-project-overview)
2. [Code Structure](#-code-structure)
3. [Algorithm Implementation](#-algorithm-implementation)
4. [Usage and Manual](#--Usage-and-Manual)
5. [Testing and Validation](#-testing-and-validation)
6. [Complete Demo in Self Run mode](#-complete-demo)


---

### 🌟 Project Overview
Our team project focuses on the implementation and demonstration of the **ElGamal and RSA encryption algorithms**. Consisting of 4 members, we have developed a Python-based application that enables users to perform encryption, decryption, and simulate eavesdropping (Eve) for both algorithms.

---

### 🗂 Code Structure
**Project/root Folder**
- `Controller.py`: Main function to initiate the application
- `elGamalAlgorithm.py`: Implements the ElGamal encryption system
- `rsaAlgorithm.py`: Implements the RSA encryption system

**Project/util Folder**
- `factorizationAlgorithm_PR.py`: Number factorization functions
- `keyGenerator_BSGS.py`: Baby-step Giant-step algorithm
- `modularArithmetic.py`: Modular arithmetic operations
- `primalityTest_MR.py`: Miller-Rabin primality test
- `pseudorandomGenerator_BBS.py`: Blum-Blum-Shub generator
- `pseudorandomGenerator_NR.py`: Naor-Reingold generator

**Project/tests Folder**
- Various test files for each module in the util folder

---

### 🚀 Deliverables: Cryptography
The project is available on GitHub:
🔗 [proteekbose/team_Elgamal-RSA](https://github.com/proteekbose/team_Elgamal-RSA)

---

### 🧮 Algorithm Implementation

**ElGamal Encryption**
- **Alice's Role (Encryption Process):**
  - Generates public information
  - Encrypts messages using ElGamal encryption

- **Bob's Role (Decryption Process):**
  - Generates public information
  - Decrypts messages received from Alice

- **Eve's Role (Eavesdropping):**
  - Intercepts encrypted messages
  - Attempts to decrypt messages without a private key

**RSA Encryption**
- Similar roles and processes as ElGamal but within the context of RSA encryption

**👀 Complete Demos Available in the Application**

---

### 💻 Usage and Manual
**Installation Requirements**
- Python 3.6 or higher
- PyCharm IDE (Recommended)

**Running the Algorithms**
1. Open `controller.py` in PyCharm
2. Run `controller.py` to start the application
3. Follow on-screen prompts to use the functions

**Executing Unit Tests**
- Run individual test files in the `util` folder from PyCharm
- Aim for close to 100% test coverage

---

### 🔍 Testing and Validation
- Detailed test cases are available in the `tests` folder
- Each utility in the application has been rigorously tested and coverage report has been generated as shown below.

![image](https://github.com/proteekbose/team_Elgamal-RSA/assets/147191386/78745df1-e570-479b-913b-64be60500814)

---
### Complete Demo
Complete Demo of El-Gamal
-----------------------------
Choose your Cipher algorithm: 

Press (1) for RSA
Press (2) for El-Gamal
Press (0) to Exit
2
------------------------------------------
    Welcome to EL-GAMAL crypto system     
------------------------------------------

Choose the role which you want to play:

Press (1) for Alice
Press (2) for Bob
Press (3) for Eve
Press (4) for COMPLETE DEMO
Press (0) to Exit 
4

🌠 Starting EL-GAMAL DEMONSTRATION... 🌠
🎲 Selecting Random Generator: Blum-Blum-Shub

🔑 Alice and Bob agree on Prime Number: 16525603 and Generator: 8789254

🔏 Alice's Secret Number: 2345641 ➡️ Public Key: 10302720
🔏 Bob's Secret Number: 12721789 ➡️ Public Key: 9434458

⚙️ Generating Message...

🔐 Encrypted Message: (c1: 15794331, c2: 1055362)
📨 Alice sends encrypted message: (c1: 15794331, c2: 1055362) to Bob
🔓 Decrypted Message: 1055068
📬 Bob decrypts the message: 1055068

🕵️‍♀️ Eve intercepts the message and attempts to decrypt it...
🔓 Decrypted Message: 1055068
Eve's cracked secret numbers: 2345641, 12721789
🔓 Eve decrypts the message: 1055068

🌈 EL-GAMAL DEMONSTRATION COMPLETED SUCCESSFULLY! 🎉

---

Complete demo of RSA
-----------------------------
Choose your Cipher algorithm: 
Press (1) for RSA
Press (2) for El-Gamal
Press (0) to Exit
1
-------------------------------------
    Welcome to RSA crypto system     
-------------------------------------
Choose the actions that you want to take:

Press (1) to Encrypt
Press (2) to Decrypt
Press (3) to Crack
Press (4) to Generate Keys
Press (5) for COMPLETE DEMO
Press (0) to Exit

Please select a function: 5

🚀 Starting RSA Demonstration...
🔐 Generating random keys...

👩‍💼 Alice's public key: (modulus: 29872450479757, exponent: 14898640488357)
🔑 Alice's private key: (modulus: 29872450479757, exponent: 5729604034733)

👨‍💼 Bob wants to send message '10046951654682' to Alice.
🔒 Bob encrypts the message using Alice's public key.
💬 The encrypted ciphertext is: 17735848996268

📩 Alice receives the encrypted message and decrypts it with her private key.
🔓 She gets the plaintext: 10046951654682

🕵️‍♀ Eve also knows the encrypted message sent to Alice;
🔨 She attempts to crack it without the private key.
🧮 Calculating the factors of the modulus, Eve finds 3301481 and 9048197
These are prime factors of the modulus 29872450479757
🔓 Eve now can find Alice's private key (modulus: 29872450479757, exponent: 5729604034733)
🕵️‍♀ Eve decrypts the message: 10046951654682

✅ RSA Demonstration Finished.

---

🌐 GitHub Repository: [Team ElGamal-RSA](https://github.com/proteekbose/team_Elgamal-RSA)

---

> **Note:** For detailed instructions, screenshots, and additional information, please refer to the individual sections in the repository's wiki or the project documentation.
