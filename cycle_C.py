import math
a,b=map(int, input().split())
min_a=False; min_b=False;i=1;mult=0
if a<0: min_a=True;
if b<0: min_b=True;
a=math.fabs(a); b=math.fabs(b)
while i<=b:
	mult+=a
	i+=1
if min_a==True and min_b==True: 
	print("(-"+str(int(a))+")*(-"+str(int(b))+")="+str(int(mult)))
elif min_a==True : 
	mult=(-1)*mult;
	print("(-"+str(int(a))+")*"+str(int(b))+"="+str(int(mult)))
elif min_b==True : 
	mult=(-1)*mult;
	print(str(int(a))+"*(-"+str(int(b))+")="+str(int(mult)))
else : print(str(int(a))+"*"+str(int(b))+"="+str(int(mult)))

