def dic_val():
	lis=[]
	for c in range (1,21,1):
		lis.append(c*c)
	for c in range (15,20):
		print(lis[c],end=" ")
	return lis
dic_val()