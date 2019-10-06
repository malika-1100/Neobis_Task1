n=int(input())
a=list(map(int, input().split()))
k=int(input()); test=False;count=0
for i in range(len(a)-k+1):
    if a == sorted(a): test=True; break;
    if a[i] > a[i+k]:
        count+=1
        a[i],a[i+k] = a[i+k],a[i]
if test: print(count)
else: print(-1)
    
    
