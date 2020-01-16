a=input()
lis =list(a.split(","))
li=[]
arr=[]
for s in lis:
	li.append(int(s))
for i in range(li[0]):
	ls=[]
	for j in range(li[1]):
		ls.append(i*j)
	arr.append(ls)	
print(arr)	

