def fromOct(s):
    count=0;num=0;
    for i in reversed(s):
        num+=int(i)*8**count;
        count+=1
    return(num)
    
def toOct(num):
    s=""
    while num>0:
        s+=str(num%8)
        num//=8
    return ''.join(reversed(s))
    
a,b = map(str,input().split())
print(toOct(int(fromOct(a))+int(fromOct(b))))
