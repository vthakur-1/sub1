a=input()
b=a.split(",")
print([int(x)*int(x) for x in b if int(x)%2 == 0])