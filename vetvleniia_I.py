import math
def length(x1, y1, x2, y2):
	x1 = int(x1); y1 = int(y1); x2 = int(x2); y2 = int(y2);
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	
x1, y1, x2, y2, x3, y3 = map(int,input().split())
ab = float(length(x1,y1,x2,y2))
bc = float(length(x2,y2,x3,y3))
ca = float(length(x3,y3,x1,y1))

x1, y1, x2, y2, x3, y3 = map(int,input().split())
ab1=float(length(x1,y1,x2,y2))
bc1=float(length(x2,y2,x3,y3))
ca1=float(length(x3,y3,x1,y1))

if ab == ab1 :
	if bc == bc1 and ca == ca1: print("YES")
	elif bc == ca1 and ca == bc1: print("YES")
	else: print("NO")
elif ab == bc1 :
	if bc == ca1 and ca == ab1: print("YES")
	elif bc == ab1 and ca == ca1: print("YES")
	else: print("NO")
elif ab == ca1 :
	if bc == ab1 and ca == bc1: print("YES")
	elif bc == bc1 and ca == ab1: print("YES")
	else: print("NO")
else: print("NO")
