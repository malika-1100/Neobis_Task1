def gcd(a,b): 
    if(b==0): return a 
    else: return gcd(b,a%b)
def lcm(a,b):
   lcm = (a*b)//gcd(a,b)
   return lcm
   
x,y=map(int,input().split())
print("GCD "+str(gcd(x,y)))
print("LCM "+str(lcm(x,y)))

