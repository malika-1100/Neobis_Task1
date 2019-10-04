import math
a,n = map(int, input().split())
prime = []
for i in range(a, n):
    for j in range(2, i):
        if i % j == 0: break
    else:
        print(i,end = ' ')
