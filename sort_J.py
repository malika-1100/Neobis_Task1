n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    temp = a[i]
    j = i - 1
    while j >= 0 and temp < a[j]:
        a[j+1], a[j] = a[j], a[j+1]
        j -= 1
        print(" ".join(map(str,a)))
