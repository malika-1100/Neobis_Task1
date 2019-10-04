n=int(input())
if n<0: print("ERROR")
else:
    n1=0; n2=1; i=1;summa=0; count=0
    while i<n:
        summa+=i
        n1=n2; n2=i
        i=n1+n2
    print(str(summa))
