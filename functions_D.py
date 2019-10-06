def perfun(n):
    i=1;summa=0;
    while i<n:
        if n%i==0 : summa+=i
        i+=1 #print(summa)
    if summa==n: return True;
    else: return False
if perfun(int(input())): print("YES")
else : print("NO")
