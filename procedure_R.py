def toOct(s):
    count=0;num=0;
    for i in reversed(s):
        if i=='1': num+=2**count;
        count+=1
    s="";
    while num>0:
        s+=str(num%8)
        num//=8
    print(s)
toOct(input())
