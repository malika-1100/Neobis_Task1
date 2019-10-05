def gcd(a,b):
    if a == 0 or b==0: 
        print("GCD("+str(a)+","+str(b)+")"); 
        if a: return a; 
        else :return b;
    elif a>b: print("GCD("+str(a)+","+str(b)+")"); return gcd(a-b,b);
    else: print("GCD("+str(a)+","+str(b)+")"); return gcd(b-a,a);
    
    
a,b=map(int,input().split())
if(a>b): ans =gcd(a-b,b)
else: ans=gcd(b-a,a);
print("GCD("+str(a)+","+str(b)+")="+str(ans))
