a=input()
lis =list(a.split(","))
lis.sort()
c=0
for l in lis:
	c+=1;
	if(c<len(lis)):
		print(l,end=",")
	else :
		print(l,end="")