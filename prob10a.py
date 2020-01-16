a=input()
lis =list(a.split(","))
lis.sort()
n=set(lis)
for j in n:
	print(j,",",end="")