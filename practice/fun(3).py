def fun(n):
    print(n-1)
    if n<0:
        return "1"
    if n==0:
        return"2"
    else:
        return fun(n-1)
print(fun(3))