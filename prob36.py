def dic_val():
	dic={}
	for c in range (21):
		dic[c]=c*c
	for c in range (5):
		print(dic[c],end=" ")
	return dic
dic_val()
