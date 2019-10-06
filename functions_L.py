def election(x,y,z):
    if x and y and z: return 1;
    elif x and y and not z: return 1;
    elif x and not y and z:  return 1;
    elif not x and y and z: return 1;
    else: return 0
    
n = int(input()); s=[]
for i in range(n):
    a, b, c = map(int, input().split())
    s.append(election(a,b,c))
for i in s:
    if i==1: print(1)
    else: print(0)
