testc=int(input())
numofcheck=int(input())
B=[]
temp=0
A=[]
prin=input()
pain=input()
lpa=prin.split(" ")
lpr=pain.split(" ")
del lpa[-1]
for v in lpa:
    q=int(v)
    A.append(q)
for v in lpr:
    q=int(v)
    B.append(q)
print(A)
print(B)
def istrue(pos,A):
    for i in range(pos+1,len(A)):
        if A[pos]>=A[i]:
            return True
    return False
sum1=0
list3=[]
sum=0
flag = True
for i in range (len(A)-1):
   if flag==False:
       flag=True
       continue
   if  A[i]>A[i+1]:
      sum+=B[i]
   else:
      if istrue(i,A):
         list3.append((A[i]*(sum+B[i]+B[i+1])))
         sum=0
         flag=False         
      else:
          for j in range(i,len(A)):
              sum+=B[j]
          list3.append(A[i]*(sum))
          break
      sum=0
print(list3)      
for i in range (len(list3)):
  sum1=sum1+list3[i]
  print(list3[i])
print(sum1)