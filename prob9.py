print("number of lines want to capilatize")
t=int(input())
ls=[]
# tr=''
for i in range (t):
	a=input()
#	tr=a.split(" ") 
	ls.append(a)	
for item in ls:
	print(item.upper())	