import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from stegano import lsb

IMAGE_PATH = "<Input Image Path>"
STEGANO_IMAGE_PATH = "<Output Image Path>"

# Step 1: Generate RSA Key Pair (Private & Public)
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Save the private key
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save the public key
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("RSA Key Pair Generated & Saved!")

# Step 2: Sign the Image Using Private Key
def sign_image():
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Read image data
    with open(IMAGE_PATH, "rb") as img:
        image_data = img.read()

    # Hash the image
    image_hash = hashlib.sha256(image_data).digest()

    # Sign the hash with RSA private key
    signature = private_key.sign(
        image_hash,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    # Save the signature
    with open("signature.sig", "wb") as f:
        f.write(signature)

    print("Image Signed Successfully!")
    return signature.hex()

# Step 3: Embed Signature Inside Image Using LSB Steganography
def embed_signature(signature_hex):
    lsb.hide(IMAGE_PATH, signature_hex).save(STEGANO_IMAGE_PATH)
    print(f"Signature Embedded in Image: {STEGANO_IMAGE_PATH}")

# Step 4: Extract & Verify Signature
def verify_signature():
    # Load Public Key
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Extract hidden signature
    hidden_message = lsb.reveal(STEGANO_IMAGE_PATH)
    extracted_signature = bytes.fromhex(hidden_message)

    # Recalculate image hash
    with open(IMAGE_PATH, "rb") as img:
        original_hash = hashlib.sha256(img.read()).digest()

    # Verify the signature
    try:
        public_key.verify(
            extracted_signature,
            original_hash,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("Signature Verified! Image is Authentic.")
    except:
        print("Signature Mismatch! Image may have been altered.")

# Run the process
if __name__ == "__main__":
    generate_keys()
    signature_hex = sign_image()
    embed_signature(signature_hex)
    verify_signature()
