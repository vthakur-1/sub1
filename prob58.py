ls=[23,45644,234,342,234,42,43,234,23,2354,756]
temp=[]
for x in ls: 
	if x not in temp:
		temp.append(x)
print(temp)		