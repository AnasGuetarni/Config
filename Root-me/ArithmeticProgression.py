import re, requests

def arith_func(n, sign, alpha, beta, u0):
    result = u0
    if n == 0:
        return u0
    if sign == '-':
        for i in xrange(1,n+1):
            result = alpha + result - (i-1)*beta
    else:
        for i in xrange(1,n+1):
            result = alpha + result + (i-1)*beta
    return result

s = requests.Session()
r = s.get('http://challenge01.root-me.org/programmation/ch1/ch1.php')
source = r.text.encode('utf-8')
match = re.search(r'U<sub>n\+1</sub> = \[ (.*) \+ U<sub>n</sub> ] (.) \[ n \* (.*) ]<br />\nU<sub>0</sub> = (.*)\n', source)
alpha = int(match.group(1))
sign = match.group(2)
beta = int(match.group(3))
u0 = int(match.group(4))
match = re.search(r'You must find U<sub>(.*)</sub>', source)
n = int(match.group(1))
result = arith_func(n, sign, alpha, beta, u0)

r = s.get('http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='+str(result))
source = r.text.encode('utf-8')
print source
