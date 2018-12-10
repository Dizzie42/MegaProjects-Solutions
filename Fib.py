n = int(input("enter number to Fib: "))


def Fib(s):
	if s < 2:
		return s
	return Fib(s-1) + Fib(s-2)


print(Fib(n))