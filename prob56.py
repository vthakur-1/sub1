a=int(input())
def gen(a):
	n=1
	while n<=a:
		if n % 5 == 0 and n % 7 == 0:
			yield n
		n+=1
b=gen(a)		
for i in gen(a):
	print(next(b))

