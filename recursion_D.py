def recur(num,n):
    if n == 0: print("1");return 1
    else: print(str(num)+"*",end=""); return num * recur(num, n - 1)

num,n=map(int,input().split());
print(recur(num,n))
