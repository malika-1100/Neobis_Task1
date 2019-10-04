def toBin(s):
    count=0;num=0;
    for i in reversed(s):
        num+=int(i)*8**count;
        count+=1
    s=""; #print(num)
    while num>0:
        s+=str(num%2)
        num//=2
    if num: s+=num
    print(''.join(reversed(s)))
toBin(input())
