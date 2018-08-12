from sympy.ntheory import factorint

n = 97569688249541945623939
message = 3485902873
e = 497

def extended_euler(a,b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = extended_euler(b % a, a)
		return (gcd, y - (b // a) * x, x)

i = next(iter(factorint(n)))
inv = (i-1)*((n/i)-1)
d = extended_euler(inv,e)[2]%inv
print pow(long(message),long(d),long(n))