dic={}
a=int(input())
def dic_val(a):
	for c in range (a+1):
		dic[c]=c*c
		print(dic[c],end=" ")
dic_val(a)
