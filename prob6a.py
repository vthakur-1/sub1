import math
def square_root(D):
	C=50
	H=30
	return math.sqrt((2 * C * D)/H)
values=input() 
lis =list(values.split(","))

for s in lis:

	res=square_root(int(s))
	print(round(res),end=",")