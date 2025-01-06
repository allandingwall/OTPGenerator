import secrets

if __name__ == "__main__":
    msg = b"Hello world!"
    key = secrets.token_bytes(128)
    enc_msg = bytes([msg[i] ^ key[i] for i in range(len(msg))])

    print(f"Message: {msg}")
    print(f"Key: {key[:len(msg)]}")
    print(f"Encrypted Message: {enc_msg}")

    dec_msg = bytes([enc_msg[i] ^ key[i] for i in range(len(enc_msg))])
    print(f"Decrypted Message: {dec_msg}")