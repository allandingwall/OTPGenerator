import secrets
import base64

def encrypt(plaintext, key):
    cipher = bytes([plaintext[i] ^ key[i] for i in range(len(plaintext))])
    cipher = bytes_to_base64(cipher)
    return cipher

def decrypt(cipher, key):
    pass

def generate_key():
    pass

def bytes_to_base64(byte_str):
    return base64.b64encode(byte_str)

def base64_to_bytes(base64_str):
    return base64.b64decode(base64_str)

if __name__ == "__main__":
    msg = b"Hello world!"
    key = secrets.token_bytes(128)
    enc_msg = encrypt(msg, key)

    print(f"Message: {msg}")
    print(f"Key: {key[:len(msg)]}")
    print(f"Encrypted Message: {enc_msg}")

    dec_msg = bytes([enc_msg[i] ^ key[i] for i in range(len(enc_msg))])
    print(f"Decrypted Message: {dec_msg}")