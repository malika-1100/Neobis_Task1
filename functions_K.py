def fromBin(s):
    count=0;num=0;
    for i in reversed(s):
        if i=='1': num+=2**count;
        count+=1
    #print(num)
    return num
def fromOct(s):
    count=0;num=0;
    for i in reversed(s):
        num+=int(i)*8**count;
        count+=1
    #print(num)
    return num
s1,s2 = map(str,input().split())
print(fromBin(s2) + fromOct(s1))
