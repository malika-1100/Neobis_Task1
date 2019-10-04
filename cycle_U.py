num=input()
chet=0;nechet=0
for value in num:
	if int(value)%2 : nechet+=1
	else: chet+=1
print(nechet, chet)
