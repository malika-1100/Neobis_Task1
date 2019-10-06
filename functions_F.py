def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def test(n):
    i=10
    while i<=n:
        #print(n%i, n//i)
        if not isPrime(n%i) and not isPrime(n//i): return False
        i*=10
    return True;
res = (test(int(input())))
if res: print("YES")
else: print("NO")
