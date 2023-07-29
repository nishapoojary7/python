def fn(n):
    if n==0:
        return 1
    else:
        return n*fn(n-1)
n=int(input("enter the number"))
print(fn(n))
