n=int(input()); 
a = list(map(int, input().split()))
first = a[0:n//2]; second = a[n//2:n]; 
a=[]
first.sort(); second.sort();second.reverse()
a=first; a.extend(second)
print(' '.join(map(str, a)))
