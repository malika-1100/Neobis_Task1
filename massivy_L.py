def shifr(s):
    ch=""; nech="";summa=0
    for i in range(len(s)):
        if i%2==0 : nech+=s[i]; 
        else : ch+=s[i];
    nech+=ch; #print(nech)
    for i in range(len(s)):
        if s[i]==nech[i]: summa+=1
    return summa  
print(shifr(input()))
