# One-Time Pad CLI Tool
A Python-based Command-Line Interface (CLI) for encrypting and decrypting files using a one-time pad. This tool generates a secure key for each encryption, stores it separately, and deletes it after decryption to prevent reuse.

## Features
- Encrypt files with a unique, securely generated key.
- Decrypt files using the provided key file.
- Automatically deletes the key after decryption.

## Usage
Encrypt a file:
```bash
./otp.py -e -i [input_file] -o [encrypted_file]
```

### Note
This tool is a work in progress, and is currently being rewritten from an earlier version that used integer representations of letters rather than bytes.
