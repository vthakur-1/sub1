sq=input()
lis=[]
tup=()
var=''
for i in sq:
	if i == ",":
		lis.append(int(var))
		
		var=''
		continue
	var=var+i
lis.append(var)
print(lis)	
print(tuple(lis))
