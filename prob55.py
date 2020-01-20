a=int(input())
def gen():
	n=1
	while n<=a:
		if n % 2 == 0:
			yield n
		n+=1	
val=gen()
for i in val:
	print(i)