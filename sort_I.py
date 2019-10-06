n,m = map(int,input().split())
a = []; count=0
for i in range(n):
    temp = []
    temp = list(map(int, input().split()))
    a.extend(temp)
kolvo = int(input())
mess = list(map(int,input().split()))
a.sort(); mess.sort()
for i in range(len(mess)):
    for j in  range(len(a)):
        if mess[i]<=a[j]: 
            count+=1; mess[i]=0; a[j]=0; break;
print(count)
