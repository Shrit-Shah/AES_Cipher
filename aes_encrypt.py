# Code Snippets reference: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/, 
# Code reference for Command Line Arguments: https://docs.python.org/3/library/argparse.html


import os,argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

parser = argparse.ArgumentParser()
parser.add_argument('KEY', help='AES 128-bit key')
parser.add_argument('MODE', choices=['ecb', 'cbc', 'gcm'], help='mode of operation')
parser.add_argument('IN', help='plain text file')
parser.add_argument('OUT', help='cipher file')
iv_file = None
parser.add_argument('--IV', dest='iv_file', help='file containing IV', required=False)
parser.add_argument('--gcm_arg', dest='gcm_auth', help='Auth Data for GCM', required=False)
args = parser.parse_args()

mode = args.MODE
output_file = args.OUT
auth_data = bytes(args.gcm_auth, 'utf-8')

with open(args.KEY, 'rb') as f:
    key = f.read()

with open(args.IN, 'rb') as f:
    plain_text = f.read()
print("Plain Text: ",plain_text)

if args.iv_file is None:
    iv = os.urandom(16)
else:
    with open(args.iv_file, 'rb') as f:
        iv = f.read()


padder = padding.PKCS7(128).padder()
padded_data = padder.update(plain_text) + padder.finalize()

if mode == 'ecb':
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    print("Encryption Mode: ECB")
elif mode == 'cbc':
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    print("Encryption Mode: CBC")
elif mode == 'gcm':
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
    print("Encryption Mode: GCM")

encryptor = cipher.encryptor()
if mode == 'gcm':
    encryptor.authenticate_additional_data(auth_data)
    print("GCM Auth Data: ",auth_data)
ct = encryptor.update(padded_data) + encryptor.finalize()

print ("Cipher text in Hex: ", ct.hex())
print ("Auth_Tag in Hex: ", encryptor.tag.hex())
with open(output_file, 'wb') as f:
    f.write(ct)