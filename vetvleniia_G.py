a,b,c=map(int, input().split())
if a+b+c == 180: 
	if a==0 or b==0 or c==0:print("NO")
	else: print("YES")
else: print("NO")
