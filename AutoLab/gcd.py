def gcd(a,b):
    a = abs(a)
    b = abs(b)           
    if(a==b):
        return b
    elif(b>a):
        a,b = b,a
        if b==0:
            return a
        return gcd(b,a%b)
    else:
        if b==0:
            return a
        return(gcd(b,a%b))