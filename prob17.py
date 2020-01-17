ls=[]
for x in range(4):
    ls.append(input().replace(' ',''))
bal=0
for x in ls:
    if x[0]=='D':
        x=x.replace('D','')
        bal+=int(x)

    if x[0]=='W':
        x=x.replace('W','')
        bal-=int(x)
print(bal)
