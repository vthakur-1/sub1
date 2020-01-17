inpr=input()
liss=inpr.split(",")
num1=int(liss[0])
num2=int(liss[1])
if num1>=1000 and num2<=3000:
	for inter in range(num1,num2):
		f=0
		for inter2 in str(inter):
			if int(inter2) % 2 != 0:
				f=1
				break
		if(f==0):
			print(inter,end=",")	
else:
	print("entre number between given range")	
