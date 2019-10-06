n,x = map(int, input().split())
a = list(map(int, input().split()))
a.sort(); count=1;
print(" ".join(map(str, a)))
mid = len(a)//2; low = 0; high = len(a)-1
 
while a[mid] != x and low <= high:
    count+=1
    if x > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print("NO "+str(count-1))
else:
    print("YES "+str(count))
