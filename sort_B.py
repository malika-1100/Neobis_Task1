n=int(input()); 
a = list(map(int, input().split()))
print(len(set(a)))
a.sort()
print(' '.join(map(str, a)))

