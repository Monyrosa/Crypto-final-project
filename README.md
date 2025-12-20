# Crypto Final Project – Secure Image Steganography

## 📌 Project Overview
This project implements a **secure image steganography system** that hides secret text messages inside digital images using the **Least Significant Bit (LSB)** technique.  
To improve confidentiality, the secret message is **encrypted with a password** before being embedded.

The system provides **two interfaces**:
- **Command-Line Interface (CLI)** using `main.py`
- **Graphical User Interface (GUI)** using `gui.py` (recommended for demo)

---

## 🎯 Objectives
- Hide secret messages inside images without visible changes
- Protect hidden messages using password-based encryption
- Combine **cryptography** and **steganography**
- Provide an easy-to-use graphical interface

---


## 📁 Project Structure

```bash
Crypto-final-project/
│
├── main.py # CLI-based interface
├── gui.py # GUI-based interface (Tkinter)
├── encoder.py # Encrypts and hides messages
├── decoder.py # Extracts and decrypts messages
├── README.md # Project documentation
├── Encrypted-Images/ # Output images with hidden messages
└── test.jpg / test.png # Sample images
```


---

## ✨ Features

### 🔐 Security Features
- Password-based XOR encryption
- Correct password required for decoding
- End-of-message marker (`<END>`) for reliable extraction

---

### 🖼 Steganography Features
- Uses Least Significant Bit (LSB) technique
- Supports PNG, JPG, and BMP images
- PNG format recommended to avoid compression loss

---

### 🖥 GUI Features
- Encode and Decode modes
- Encode-only fields hidden in Decode mode
- Popup messages for success and errors
- Output images automatically saved in `Encrypted-Images/`

---
## ⚙️ Project Setup

### 🧰 Requirements
- Python 3.10 or higher

---

### 🛠️ Setup Instructions

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Monyrosa/Crypto-final-project.git
```

### 2️⃣ Navigate to the Project Directory
```bash
cd Crypto-final-project
```

### 3️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate it:

Windows (PowerShell)

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---

## ▶️ How to Run the Project

### 🧾 Command-Line Interface (CLI)


```bash
python main.py
```

Menu options:

1. Hide a secret message

2. Reveal a hidden message

3. Exit

---

### 🖥 Graphical User Interface (GUI) – Recommended

```bash
python gui.py
```

Encode Mode:

1. Select an image

2. Enter the secret message

3. Enter a password

4. Enter output image name (PNG)

5. Click ENCODE

Decode Mode

1. Select an encoded image

2. Enter the password

3. Click DECODE

4. Hidden message is displayed in a popup

---

### 🔍 How It Works (Technical Summary)

- The secret message is encrypted using a password

- The encrypted message is converted to binary

- Binary data is embedded into image pixel LSBs

- <END> marker indicates message termination

- Decoding extracts and decrypts the hidden message

---

## ⚠️ Limitations

- XOR encryption is for educational purposes only

- Message size depends on image resolution

- Lossy image formats may corrupt hidden data

--- 

## 📜 License
This project is open-source and intended for educational use.

---

## 🤝 Contributing
Feel free to submit issues or pull requests to enhance functionality.

---

## 📧 Contact
For questions or feedback, contact: jayyjozaa@gmail.com 

---