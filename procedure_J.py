def elem(n):
    k1=1;k2=2;k3=3;
    if n==1:return k1;
    elif n==2: return k2;
    elif n==3: return k3;
    
    for i in range(4,n+1):
        k=k3+k2-2*k1;
        k1=k2;k2=k3;k3=k; 
    return k;
    
print(elem(int(input())))

