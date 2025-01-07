import argparse
import base64
import os
import secrets

def encrypt(plaintext, key):
    cipher = bytes([plaintext[i] ^ key[i] for i in range(len(plaintext))])
    return cipher

def decrypt(cipher, key):
    plaintext = bytes([cipher[i] ^ key[i] for i in range(len(cipher))])
    return plaintext

def generate_key(key_length):
    return secrets.token_bytes(key_length)

def bytes_to_base64(byte_str):
    return base64.b64encode(byte_str)

def base64_to_bytes(base64_str):
    return base64.b64decode(base64_str)

def bytes_to_string(bytes_str):
    string = bytes_str.decode("utf-8")
    return string

if __name__ == "__main__":
    msg = b"Hello world!"
    key = secrets.token_bytes(256)
    enc_msg = encrypt(msg, key)

    print(f"Message: {msg}")
    print(f"Key: {bytes_to_base64(key[:len(msg)])}")
    print(f"Encrypted Message: {bytes_to_base64(enc_msg)}")

    dec_msg = decrypt(enc_msg, key)
    print(f"Decrypted Message: {dec_msg}")