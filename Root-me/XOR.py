#!/usr/bin/env python

def xor(s1, s2):
	global key_size
	res = [chr(0)]*key_size
	for i in range(len(s1)):
		q = ord(s1[i])
		d = ord(s2[i])
		k = q ^ d
		res[i] = chr(k)
	res = ''.join(res)
	return res

with open('ch3.bmp', 'rb') as f:
	data = f.read()

key = 'fallenfallenfallen'
key_size = len(key)
dec_data = ''
for i in range(0, len(data), key_size):
	enc = xor(data[i:i+key_size], key)
	dec_data += enc
with open('decrypted.png', 'wb') as f:
	f.write(dec_data)
