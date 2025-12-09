# Crypto-Final-Project: Image Steganography

This project focuses on hiding secret text inside digital images using image steganography. The goal is to enable secure communication without attracting attention. It is motivated by the need for privacy, data protection, and safe information exchange. The project also applies cryptography concepts such as confidentiality and data hiding.

---

## 📁 Project Structure

Crypto-Final-Project/
├── main.py # Main entry point
├── encoder.py # Handles embedding text in images
├── decoder.py # Handles extracting text from images
├── README.md # Project overview
└── (Other files and resources)

---

## 🚀 Features:
- Embed secret messages inside images using LSB (Least Significant Bit) technique
- Support for encoding and decoding messages in RGB images

---

## 🛠️ Requirements:
Ensure you have **Python 3.10+** installed.

Install dependencies using:
```bash
pip install pillow

```
## ▶️ Usage

### **1. Hide a Message in an Image:**
Run the encoding script to hide a secret message inside an image: 
```bash
python main.py
```
Follow the prompts:
- Input the image file.
- Enter the secret message.
- Define the output image file name.

---

### **2. Reveal a Hidden Message from an Image:**
Run the decoding script to extract the hidden message from the image:
```bash
python main.py
```
Follow the prompts:
- Provide the image file containing the hidden message.

---

## 📜 License
This project is open-source and free to modify or distribute.

---

## 🤝 Contributing
Feel free to submit issues or pull requests to enhance functionality.

---

## 📧 Contact
For questions or feedback, contact: jayyjozaa@gmail.com 

