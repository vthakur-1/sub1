input_value =int(input())
st = "a+aa+aaa+aaaa";
sum=0
st = st.replace("a",str(input_value))
l=st.split("+")
for i in l:
	sum+=int(i)
print(sum)