def year(n):
    if n%100==0  and n%400!=0: return "NO"
    elif n%4==0: return "YES"
    else: return "NO"
print(year(int(input())))
