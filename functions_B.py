def summ(n):
    summa=0
    for i in reversed(n):
        summa+=int(i)
        if i==n[0] : print(i+"=",end="")
        else : print(i+"+",end="")
    print(str(summa))
summ(input())
