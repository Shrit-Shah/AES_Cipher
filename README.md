# AES Encryption and Decryption

This set of Python scripts, `aes_encrypt.py` and `aes_decrypt.py`, demonstrate AES (Advanced Encryption Standard) encryption and decryption using the cryptography library. These scripts support different modes of operation such as ECB (Electronic CodeBook), CBC (Cipher Block Chaining), and GCM (Galois/Counter Mode).

## Dependencies

Make sure to install the required dependencies using the following:

```bash
pip install cryptography
```
## AES Encryption Script - aes_encrypt.py
### Usage
```bash
python aes_encrypt.py KEY MODE IN OUT [--IV IV_FILE] [--gcm_arg GCM_AUTH]
```
- KEY: AES 128-bit key file.
- MODE: Mode of operation (ecb, cbc, or gcm).
- IN: Input plain text file.
- OUT: Output cipher text file.
- --IV IV_FILE: File containing the Initialization Vector (IV) for CBC and GCM modes (optional).
- --gcm_arg GCM_AUTH: Authentication Data for GCM mode (optional).
### Example
```bash
python aes_encrypt.py keyfile.txt cbc plaintext.txt ciphertext.txt --IV ivfile.txt
```
## AES Decryption Script - aes_decrypt.py
### Usage
```bash
python aes_decrypt.py KEY MODE IN OUT [--IV IV_FILE] [--gcm_arg GCM_AUTH] [--gcm_tag GCM_TAG]
```
- KEY: AES 128-bit key file.
- MODE: Mode of operation (ecb, cbc, or gcm).
- IN: Input cipher text file.
- OUT: Output decrypted text file.
- --IV IV_FILE: File containing the Initialization Vector (IV) for CBC and GCM modes (optional).
- --gcm_arg GCM_AUTH: Authentication Data for GCM mode (optional).
- --gcm_tag GCM_TAG: GCM tag in HEX created during encryption (required for GCM mode).
###Example
```bash
python aes_decrypt.py keyfile.txt cbc ciphertext.txt decrypted.txt --IV ivfile.txt --gcm_arg authdata --gcm_tag gcm_tag_hex
```
## Note
- The scripts utilize the cryptography library for AES encryption and decryption.
- GCM mode requires additional authentication data and the GCM tag from the encryption process.
- For more details on cryptography.io, refer to the documentation.
