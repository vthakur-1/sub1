a=input()
p=0
i=0
for s in a:
	if ord(s) in range (65,91):
		p+=1
	if ord(s) in range(97,123):
		i+=1
print("number of big letter",p)
print("number of small letter",i)