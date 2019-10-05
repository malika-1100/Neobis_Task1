def recur(n,summa):
    if n//10 == 0 : 
        if n%10 : print(str(n%10)); summa+=n%10; return summa;
    else: print(str(n%10)+"+",end=""); summa+=n%10; return recur(n//10,summa)

print(recur(int(input()),0))
