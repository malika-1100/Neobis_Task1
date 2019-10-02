anton,boris,victor=map(int,input().split())
if anton == boris and boris == victor : print("Same age")
elif anton == boris or anton == victor or boris == victor :
		if anton==boris and boris > victor or boris < victor : print("Victor")
		elif anton==victor and victor>boris  or victor<boris: print("Boris")
		elif victor==boris and boris>anton or boris<anton: print("Anton")
		
else:
	maximum=max(anton,max(victor,boris))
	if maximum==anton: print("Anton")
	elif maximum==victor: print("Victor")
	else : print("Boris")
