#Convert decimal to binary or binary to decimal
import math

def bin_to_dec(num):
	r=1
	binary_answer = []
	num=int(num)
	while(num > 0):
		r = num%2		#remainder
		num = num/2		#reset num
		num = math.floor(num)
		binary_answer.append(r)
		
	binary_answer.reverse()	
	return ''.join(str(e) for e in binary_answer)	
	

def dec_to_bin(num):
	p = 0
	result=0
	i=1
	length = len(num)
	
	while(i <= length):
		currentDigit = num[-i]
		result += int(currentDigit)*(2**p)
		p += 1
		i += 1
	return result
	
	
while(1):	
	print("""
		1. Binary to Decimal Conversion
		2. Decimal to Binary Conversion
		0. End the program\n""")

	choice = input("Choose conversion type: ")	

	if int(choice) == 1:
		number = input("Number to convert: ")
		print("Decimal of %s is %s" % (number, dec_to_bin(number)))
	elif int(choice) == 2:
		number = input("Number to convert: ")
		print("Binary of %s is %s" % (number, bin_to_dec(number)))
	elif int(choice) == 0:
		print("Ending...")
		break;
	else:
		print("Invalid Choice")