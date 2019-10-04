def toHex(s):
    count=0;num=0;
    for i in reversed(s):
        if i=='1': num+=2**count;
        count+=1
    s="";#print(num)
    while num>0:
        if num%16==10: s+='A'
        elif num%16==11: s+='B'
        elif num%16==12: s+='C'
        elif num%16==13: s+='D'
        elif num%16==14: s+='E'
        elif num%16==15: s+='F'
        else: s+=str(num%16)
        num//=16
    print(s)
    
toHex(input())
