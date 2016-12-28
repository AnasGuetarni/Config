from Crypto.Cipher import AES
from Crypto import Random
import base64

def fillZero(hexStr, strLen):
	return ('0' * (strLen - len(hexStr))) + hexStr

def pkcs7pad(data):
	length = 16 - (len(data) % 16)
	data += chr(length)*length
	return data

def pkcs7unpad(data):
	return data[:-ord(data[-1])]

def aesEncrypt(key, iv, plain):
	aes = AES.new(key, AES.MODE_CBC, iv)
	print pkcs7pad(plain).encode('hex')
	return aes.encrypt(pkcs7pad(plain))

def aesDecrypt(key, iv, cipher):
	aes = AES.new(key, AES.MODE_CBC, iv)
	return pkcs7unpad(aes.decrypt(cipher))

realPlain = '''Marvin: "I am at a rough estimate thirty billion times more intelligent than you. Let me give you an example. Think of a number, any number."
Zem: "Er, five."
Marvin: "Wrong. You see?"'''[:16]
cipher = base64.b64decode('cY1Y1VPXbhUqzYLIOVR0RhUXD5l+dmymBfr1vIKlyqD8KqHUUp2I3dhFXgASdGWzRhOdTj8WWFTJPK0k/GDEVUBDCk1MiB8rCmTZluVHImczlOXEwJSUEgwDHA6AbiCwyAU58e9j9QbN+HwEm1TPKHQ6JrIOpdFWoYjS+cUCZfo/85Lqi26Gj7JJxCDF8PrBp/EtHLmmTmaAVWS0ID2cJpdmNDl54N7tg5TFTrdtcIplc1tDvoCLFPEomNa5booC')
key = base64.b64decode('AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRqrHB0eHyA=')
iv = Random.new().read(AES.block_size)
plain = aesDecrypt(key, iv, cipher)
intmd = int(plain[:16].encode('hex'), 16) ^ int(iv.encode('hex'), 16)
realIV = fillZero(hex(intmd ^ int(realPlain.encode('hex'), 16)).replace('0x','').replace('L',''), 32).decode('hex')
print realIV
