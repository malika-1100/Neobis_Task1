def toBin(n):
    s=""
    while n>0:
        s=str(n%2)+s
        n//=2;
    while len(s)<8:
        s="0"+s
    print(s)
n=int(input())
toBin(n)
