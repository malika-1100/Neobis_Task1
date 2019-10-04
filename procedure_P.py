def toHex(s):
    count=0; num=0
    for i in reversed(s):
        if i=='A': num+=10*16**count;
        elif i=='B' : num+=11*16**count;
        elif i=='C' : num+=12*16**count;
        elif i=='D' : num+=13*16**count;
        elif i=='E' : num+=14*16**count;
        elif i=='F' : num+=15*16**count;
        else: num+=int(i)*16**count;
        count+=1
    print(num);
toHex(input())
