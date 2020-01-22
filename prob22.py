a=input()
b=a.split(" ")
b.sort()
print(b)
k=""
for i in b:
	c=0
	c=b.count(i)
	if k == i:
		continue
	print(i,":",c)	
	k=i