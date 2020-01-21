class shape():
	def area(self,length):
		pass
class square(shape):
	def __init__(self,length):
		self.length=length
	def area(self,length):
		area=length**2
		return area
a=square(27)
print(a.area(12))