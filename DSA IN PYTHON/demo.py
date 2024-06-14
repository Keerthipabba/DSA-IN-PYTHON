def fun(n,l):
    if n <= 0:
        return l
    l.append(n)
    t=fun(n-1,l)
    return(t)

print(fun(5, []))