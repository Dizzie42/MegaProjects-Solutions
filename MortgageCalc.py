#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the 
#compounding interval (Monthly, Weekly, Daily, Continually).

#No edit checks, we're lazy
terms = int(input('Enter number of months (terms): '))
int_rate = float(input('Enter an interest rate: '))
loan = float(input('Enter a loan value: '))

#Mortgage payment calc formula :
	#Mortgage_Payment = Principal [i(1+i)^n]/[(1+i)^n-1]
#i = monthly interest rate (total /12)
#n = number of payments over life of the loan


def calculate(t, i, amt):
	monthly_rate = (i/100)/12   	#/100 to get decimal, /12 for monthly
	p = amt * (monthly_rate*((1+monthly_rate)**t)) / ((1+monthly_rate)**(t)-1)
	return p;
	
	
result = calculate(terms, int_rate, loan)
print( "M. payment for a $%.2f %s year mortgage at %.2f%% int rate is: $%.2f" % (loan, (terms/12), int_rate, result) )