import math
tr=[]
c=0
w=0
for i in range(4):
	a=input()
	t=tuple(a.split(" "))
	tr.append(t)
for s in tr:
	if s[0]=="UP":
		c=c+int(s[1]) 
	if s[0]=="DOWN":
		c=c-int(s[1]) 
	if s[0]=="RIGHT":
		w=w+int(s[1]) 
	if s[0]=="LEFT":
		w=w-int(s[1])
print(round(math.sqrt(w**2+c**2))) 	