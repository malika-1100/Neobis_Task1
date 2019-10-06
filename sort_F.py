n=int(input())
a=list(map(int, input().split()))
ind = a.index(max(a))
a[0],a[ind] = a[ind],a[0]
print(' '.join(map(str, a)))   
    
