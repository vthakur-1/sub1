tup=(1,2,3,4,5,6,7,8,9,10)
def print_half(tup):
	for i in range (5):
		print(tup[i],end=" ")
	print()	
	for j in range (5,10,1):
		print(tup[j],end=" ")
print_half(tup)
	