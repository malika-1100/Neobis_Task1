n=(input())
prev=-1; test=False
for el in n:
	if el==prev: test=True; break;
	prev=el
if test: print("YES")
else: print("NO")

