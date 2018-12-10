#Change Return Program - The user enters a cost and then the amount of money given. 
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

#NOTE:  We do not care about cases where the user gives less money than the cost.  Noone does that >_<
import math

#No edit checks, we're lazy
c = float(input('Enter cost: '))
given = float(input('Enter money given: '))


def divy_change(change):
	dollar = 0
	q = 0
	d = 0
	n = 0
	p = 0								#number of Q,D,N,P due

	if (change >= 25): 			#is divisble by 25, give a quarter
		q = int(change /25);
		change = change % 25
	if (change >= 10) >= 1:
		d = int(change /10);
		change = change % 10
	if (change >= 5) >= 1:
		n = int(change /5);
		change = change % 5
	if (change >= 1) >= 1:
		p = int(change /1);
		change = change % 1
		
		
	return q, d, n, p
	

def calc_change(cost, given):		#returns amount of change due as float
	due = (given-cost)*100			#floats suck
	return divy_change(due);						
	
	
	
q, d, n, p = calc_change(c, given);
print( "\nNumber of Quarters " + str(q) + "\nNumber of Dimes " + str(d) + "\nNumber of Nickels " + str(n) + "\nNumber of Pennies " + str(p))