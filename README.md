### Note ⚠️⚠️
This tool is currently a work in progress, and is currently being rewritten from an earlier toy implementation (otp-generator.py) that used integer representations of letters rather than bytes.

# One-Time Pad CLI Tool
This is a Python-based Command-Line Interface (CLI) for encrypting and decrypting files using a one-time pad. This tool generates a secure key for each encryption, stores it separately, and deletes it after decryption to prevent reuse.

## Features
- Encrypt files with a unique, securely generated key.
- Decrypt files using the provided key file.
- Automatically deletes the key after decryption.

## Usage
Encrypt a file:
```bash
./otp.py -e -i [input_file] -o [encrypted_file]
```

Decrypt a file:
```bash
./otp.py -d -i [input_file] -o [decrypted_file]
```
