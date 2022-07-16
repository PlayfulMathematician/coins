def nFlip(x,n,k):
    r=list(map((lambda t: 1),list(range(0,x)))
    if k+n>x:
        r[k:n+k]=list(map((lambda x:1-x),r[k:n+k]))
        return k
    else:
        raise ArithmeticError()
         
