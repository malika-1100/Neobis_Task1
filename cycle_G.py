n=(input())
prev=-1; test=0
for el1 in n:
	test=0
	for el2 in n:
		if el1 == el2: test+=1; 
	if test>1: break;

if test>1: print("YES")
else: print("NO")
