mass=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def fromDec(num,n,s):
    if num==0: return  "".join(reversed(s));
    else: 
        if num%n >=10: s+=str(mass[num%n-10]);
        else: s+=str(num%n);
        return fromDec(num//n,n,s)
num,n=map(int,input().split())
print(fromDec(num,n,""))
