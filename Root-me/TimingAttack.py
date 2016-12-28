import sys, socket, time

host = "challenge01.root-me.org"
port = 51015

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
key = '____________'
key_index = 0
prev_time = 0.2
c = 0
print s.recv(2024)
while(key_index < 12):
	if key_index == 5:
		k = '-'
	else:
		k = chr(48+c)
	key = key[:key_index] + k + key[(key_index+1):]
	start_time = time.time()
	s.send(key+'\r\n')
	print s.recv(2024).strip()
	print 'time:', time.time() - start_time, 'key:', key, '\r\n'
	elapse_time = time.time() - start_time
	if elapse_time - prev_time > 0.45:
		print '------------------', k
		key_index += 1
		prev_time = elapse_time
		c = 0
		continue
	c += 1
s.close()
