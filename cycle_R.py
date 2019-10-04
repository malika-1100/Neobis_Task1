num=input()
i=1; new=""
for value in num:
	if i!=1 and i!=len(num): new+=value
	i+=1
	
print(new)
