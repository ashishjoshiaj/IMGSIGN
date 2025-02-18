## For overall_code.py
This project is implemented as image authentication by signing them with RSA(Rivest–Shamir–Adleman) encryption and verifying the authenticity using LSB (Least Significant Bit) steganography. It also hides and reveals - secret messages in the pictures.

Features:

Generate RSA Key Pair
Sign the Image using **SHA-256**.
Embed & Verify Signature via **steganography**.
Hide & Extract **Secret Messages**.

Execution:
```python
   python overall_code.py
   ```

## For secret.py
## Overview
This script hides and extracts secret messages using LSB steganography.

## Features
- **Hide a message** inside an image.
- **Extract the hidden message** from the modified image.

## Execution
1. **Hide a Message**  
   ```python
   python secret.py
   ```
   Saves the modified image with the hidden text.

2. **Reveal the Message**  
   ```python
   python secret.py
   ```
   Extracts and prints the hidden text.


## Author  
Ashish Joshi
