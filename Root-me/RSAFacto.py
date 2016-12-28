from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from sympy.solvers import solve
from sympy import Symbol
import libnum, base64

'''
inspect file .pem to find e, n with below command
openssl rsa -pubin -in pubkey.pem -text -modulus
and use factordb.com to find prime factor from n(modulus)
'''

def decrypt(p, q, e, n, ct):
	phi = (p - 1 ) * (q - 1)
	d = libnum.invmod(e, phi)
	privkey = RSA.construct((n,e,d,p,q))
	#return privkey.decrypt(ct)
	return repr(privkey.decrypt(ct))

m = 'e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA'
e = 65537L
p = 398075086424064937397125500550386491199064362342526708406385189575946388957261768583317
q = 472772146107435302536223071973048224632914695302097116459852171130520711256363590397527
n = 188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059
print decrypt(p, q, e, n, m.decode('base64'))
