import math
a, b, h = map(int,input().split())
side = a + b
gipo = float(math.sqrt(a**2 + b**2))
gipo += 2*h

if gipo < side : print(int(round(gipo**2)))
else : print(side**2)
