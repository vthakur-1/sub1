v=[]
c1=[]
ls=[]
numv=[]
s=input()
count=0
num=0
w=""
k=""
def subString(s, n,ls): 
    temp=''
    for i in range(n): 
        for len in range(i+1,n+1): 
            temp = s[i: len]
            ls.append(temp) 
            temp=''
    return ls        
subString(s,len(s),ls);
b=['a','e','i','o','u']
for i in ls:
	for j in i:
		if j in b:
			k=i
			v.append(i)
			break
		else:
			c1.append(i)
			break			
v.sort()
k1=""
f1=0
for i in v:
	c=0
	c=v.count(i)
	if k1 == i:
		continue
	f1=c+f1	
	k1=i
print(f1)
c1.sort()
k1=""
f=0
for i in c1:
	u=0
	u=c1.count(i)
	if k1 == i:
		continue
	f=u+f	
	k1=i
print(f)
if f1 > f:
	print("kevin",f1)	
elif f > f1:
	print("Stuart",f)
