This project is implemented as image authentication by signing them with RSA(Rivest–Shamir–Adleman) encryption and verifying the authenticity using LSB (Least Significant Bit) steganography. It also hides and reveals - secret messages in the pictures.

Features:

Generate RSA Key Pair
Sign the Image using SHA-256
Embed & Verify Signature via steganography:
Hide & Extract Secret Messages

Execution:
1. Image Signing 
python overall_code.py
2. Image message insertion and revealing
python secret.py
