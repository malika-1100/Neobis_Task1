num=input()
n=0;
while n <= int(num):
	n+=1; test=0
	for i in str(n):
		if int(i)!=0 and int(n)%int(i)==0 : test+=1
		else: test=0; break
	if test==len(str(n)): print(str(n), end =" ")
