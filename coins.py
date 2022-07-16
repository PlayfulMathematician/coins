def nFlip(r,n,k):
    x=len(r)
    if k+n>x:
        r[k:n+k]=list(map((lambda x:1-x),r[k:n+k]))
        return r
    else:
        raise ArithmeticError()
         
def binList(x):
    if x==1:
        return [[0],[1]]
    else:
        return list(map(lambda y:[0]+y,binList(x-1)))+list(map(lambda y:[1]+y,binList(x-1)))
def sequenceOfNFlip(x,n,bin_list):
    r=list(map((lambda t: 1),list(range(0,x))))
    for i,q in enumerate(bin_list):
        if q==0:
            continue
        else:
            r=nFlip(r,n,i)
    return r
            
    
