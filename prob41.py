def dic_val():
	lis=[]
	for c in range (1,21,1):
		lis.append(c*c)
		tuple(lis)
	for c in range (1,21):
		print(lis[c-1],end=" ")
	return lis
dic_val()