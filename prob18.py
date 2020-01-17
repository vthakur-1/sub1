import re
p= input("Input your password")
a = 1

while a:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("s",p):
        break
    else:
        print("Valid Password")
        a=False
        break
if a:
	print("Not a Valid Password")
