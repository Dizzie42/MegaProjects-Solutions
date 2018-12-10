#Prime factorization - Enter a number and find all prime factors if any
#prime = number divisible by 1 and itself

import math

print("Incoming Primes...")

prime=2	

def is_prime(n):
	if n == 2:
		return True
	if n%2 == 0:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n%i == 0:
			return False		
	return True

	
def next_prime(p):
	newPrime = p + 1
	while True:
		if not is_prime(newPrime):	#if new prime is not a prime, add 1 and try again
			newPrime += 1
		else:
			break
	return newPrime
	
	
	
while input("Enter f to stop...").lower() != 'f': 
	print(prime)
	prime = next_prime(prime)




