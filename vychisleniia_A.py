a,b,c=map(int,input().split())
summa=a+b+c
mult=a*b*c
sred= float('{:.3f}'.format(summa/3))
print(str(a)+"+"+str(b)+"+"+str(c)+"="+str(summa))
print(str(a)+"*"+str(b)+"*"+str(c)+"="+str(mult))
print("("+str(a)+"+"+str(b)+"+"+str(c)+")/3="+str(sred))
