def toHex(n):
    s=""
    while n>0:
        if n%16==10: s+='A'
        elif n%16==11: s+='B'
        elif n%16==12: s+='C'
        elif n%16==13: s+='D'
        elif n%16==14: s+='E'
        elif n%16==15: s+='F'
        else: s+=str(n%16);
        n//=16;
    print(s)
toHex(int(input()))
