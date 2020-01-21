a=int(input())
def gen():
	n=1
	while n<=a:
		if n % 2 == 0:
			print(n)
			yield n
		n+=1	
val=gen()
for i in range(1,a,1):
	next(val)