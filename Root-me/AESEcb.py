from Crypto.Cipher import AES
from Crypto import Random
import base64

'''
* First 4 bytes are unused, probably reserved for version number
* Next 20 bytes are the basis of the key, to be XORed in a loop
	until a sixteen-byte key is produced.
* The rest of the file is, repeated as necessary:
		four bytes = length of following cipher chunk, little-endian
		n bytes = cipher chunk
* Encryption is AES 128-bit ecb.
* Chunk lengths are always a multiple of 16 bytes (128 bits).
	Therefore there may be padding. We assume that any trailing byte
	containing a value less than '\n' is a padding byte.    
'''

def pkcs7pad(data):
	length = 16 - (len(data) % 16)
	data += chr(length)*length
	return data

def pkcs7unpad(data):
	return data[:-ord(data[-1])]

def aesEncrypt(key, plain):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(pkcs7pad(plain))

def aesDecrypt(key, cipher):
	aes = AES.new(key, AES.MODE_ECB)
	return pkcs7unpad(aes.decrypt(cipher))

with open('mylogin.cnf', 'rb') as f:
	data = f.read()
keylen = 20
key = data[4:4+keylen]
# xor key first 4 bytes with last 4 bytes
for i in range(4):
	key = key[:i] + chr(ord(key[i]) ^ ord(key[i+16])) + key[i+1:]
key = key[:16]

idx = 4+keylen
cipher = ''
while idx < len(data):
	cipherChunkLen = int(data[idx:idx+4][::-1].encode('hex'), 16)
	idx += 4
	cipher += data[idx:idx+cipherChunkLen]
	idx += cipherChunkLen
print aesDecrypt(key, cipher)
