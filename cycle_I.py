for value in range(100, 1000):
	num= (value%10)**3+((value%100)//10)**3+(value//100)**3
	if num==value: print(value)
