def fromBin(s):
    count=0;num=0;
    for i in reversed(s):
        if i=='1': num+=2**count;
        count+=1
    #print(num)
    return num
    
def toBin(num):
    s=""; 
    while num>0:
        s+=str(num%2);
        num//=2;
    #while len(s)%4!=0: s+='0'
    return ''.join(reversed(s))
s1,s2 = map(str,input().split())
print(toBin(fromBin(s1) * fromBin(s2)))
