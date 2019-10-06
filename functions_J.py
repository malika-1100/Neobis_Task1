def Xor(x,y):
    if x and not y: return 1;
    elif not x and y: return 1;
    else: return 0;
n = int(input()); s=[]
for i in range(n):
    a, b = map(int, input().split())
    s.append(Xor(a,b))
for i in s:
    print(i)
