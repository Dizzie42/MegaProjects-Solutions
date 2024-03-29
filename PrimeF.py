#Prime factorization - Enter a number and find all prime factors if any
#prime = number divisible by 1 and itself

import math

n = int(input("Enter number to Prime: "))

# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
	if n==0:
		return 0
	# Print the number of two's that divide n 
	while n % 2 == 0: 
		print(2,end=" ")
		n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 

        # while i divides n , print i ad divide n
		while n%i == 0:
			print(i,end=" ")
			n = n / i
              
    # Condition if n is a prime 
    # number greater than 2 
	if n > 2:
		print(int(n))

		
primeFactors(n)




