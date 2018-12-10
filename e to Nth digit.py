#eulers number
from math import e

def e_with_p(n):
	return '%.*f' % (n, e)


p = int(input('Enter # decimal places'))
print(e_with_p(p))

