a=input()
p=0
i=0
for s in a:
	if ord(s) in range (65,91) or ord(s) in range(97,123):
		p+=1
	if ord(s) in range(48,58):
		i+=1
print("number of letter",p)
print("number of numericals",i)


