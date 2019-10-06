import locale
loc=locale.getlocale()
locale.setlocale(locale.LC_ALL, ('RU','UTF8'))
n=int(input())
n1=n%10
if n1==1: print( "Вам", n, "год")
elif n>=11 and n<=20: print( "Вам", n, "лет")
elif n1==2 or n1==3 or n1==4: print( "Вам", n, "года")
else : print( "Вам", n, "лет")
