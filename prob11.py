a=input()
lis=list(a.split(","))
lisss=[]
i=0
for k in lis:
 	lisss.append(int(k,2))
 	i+=1
for g in lisss:
	if g % 5 == 0:	
 		print("{0:b}".format(g))
