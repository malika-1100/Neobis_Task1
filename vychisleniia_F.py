import math
x1,y1,x2,y2,x3,y3=map(float,input().split())

a=math.sqrt((x2-x1)**2+(y2-y1)**2)
b=math.sqrt((x3-x2)**2+(y3-y2)**2)
c=math.sqrt((x1-x3)**2+(y1-y3)**2)

p=a+b+c
s=math.fabs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))*0.5
print (round(p,5), round(s,1))
