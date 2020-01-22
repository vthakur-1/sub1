a=int(input())
class gen():
	def gent(self,a):
		n=1
		while n<=a:
			if n % 7 == 0:
				yield n
			n+=1			
obj=gen()
obj.gent(a)
for i in obj.gent(a):
	print(i)
