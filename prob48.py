lis=[]
for i in range(1,21):
	ina=i
	lis.append(ina)
a=list(filter(lambda x:x%2==0,lis))
print(a)