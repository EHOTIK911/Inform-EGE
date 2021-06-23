def F(n):
    print(n*n)
    if n > 1:
        print(2*n+1)
        F(n-2)
        F(n//3)
print(F(50))
