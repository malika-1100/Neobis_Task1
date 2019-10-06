n,x = map(int, input().split())
a = list(map(int, input().split()))
a.sort(); count=0;
print(" ".join(map(str, a)))
low = 0; high = len(a)-1
while low <= high:
    count+=1
    mid = (low + high) // 2
    if x < a[mid]:
        high = mid - 1
    elif x > a[mid]:
        low = mid + 1
    else:
        print("YES "+str(count))
        break
else:
    print("NO "+str(count))
