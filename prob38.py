def dic_val():
	lis=[]
	for c in range (1,21,1):
		lis.append(c*c)
	for c in range (5):
		print(lis[c],end=" ")
	return lis
dic_val()