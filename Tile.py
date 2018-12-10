#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a W x H floor, using a cost entered by the user.

def quest():
	cost = float(input("Cost per meter squared (m^2): "))
	width = float(input("Width of room (meters): "))
	height = float(input("Height of room (meters): "))
	
	return cost, width, height;
	

c,w,h = quest()			#floats
print("The cost is: $%.2f" % (float(c * w * h)))
