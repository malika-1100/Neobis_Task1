n=int(input())
i=1;
while i<n:
	square=i*i
	if i<10:
		if square%10 == i: print(str(i)+"*"+str(i)+"="+str(square))
	elif i<100:
		if square%100 == i: print(str(i)+"*"+str(i)+"="+str(square))
	i+=1
