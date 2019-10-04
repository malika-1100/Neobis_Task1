def gcd(a,b): 
    if(b==0): return a 
    else: return gcd(b,a%b)
a,b=map(int,input().split())
print("GCD("+str(a)+"," +str(b)+")="+str(gcd(a,b)))
