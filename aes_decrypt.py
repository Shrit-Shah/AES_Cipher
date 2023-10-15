# Code Snippets reference: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/, 
# Code reference for Command Line Arguments: https://docs.python.org/3/library/argparse.html

import os,argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

parser = argparse.ArgumentParser()
parser.add_argument('KEY', help='AES 128-bit key')
parser.add_argument('MODE', choices=['ecb', 'cbc', 'gcm'], help='mode of operation')
parser.add_argument('IN', help='cipher file')
parser.add_argument('OUT', help='decrypted file')
iv_file = None
parser.add_argument('--IV', dest='iv_file', help='file containing IV', required=False)
parser.add_argument('--gcm_arg', dest='gcm_auth', help='Auth Data for GCM', required=False)
parser.add_argument('--gcm_tag', dest='gcm_tag', help='GCM tag in HEX created while encrypting', required=False)
args = parser.parse_args()

mode = args.MODE
output_file = args.OUT
auth_data = bytes(args.gcm_auth, 'utf-8')
tag = bytes.fromhex(args.gcm_tag)

with open(args.KEY, 'rb') as f:
    key = f.read()

with open(args.IN, 'rb') as f:
    ct = f.read()
print("Cipher Text: ",ct) 
if args.iv_file is None:
    iv = os.urandom(16)
else:
    with open(args.iv_file, 'rb') as f:
        iv = f.read()


if mode == 'ecb':
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    print("Decryption Mode: ECB")
elif mode == 'cbc':
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    print("Decryption Mode: CBC")
elif mode == 'gcm':
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv,tag))
    print("Decryption Mode: GCM")

decryptor = cipher.decryptor()
if mode == 'gcm':
    decryptor.authenticate_additional_data(auth_data)
    print("GCM Auth Data: ",auth_data)
    print("GCM Tag: ",tag)
text = decryptor.update(ct) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
data = unpadder.update(text) + unpadder.finalize()

print("Decrypted Text: ",data)

with open(output_file, 'wb') as f:
    f.write(data)