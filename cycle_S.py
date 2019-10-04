num=input()
n=len(num); summa=0
if n%2==0: n/=2
for value in num:
	summa+=int(value)
	n-=1
	if --n==0: break;
print(summa)
