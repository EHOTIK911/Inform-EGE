def F(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2 and n % 2 == 0:
        return (n*F(n-1))//2
    if n > 2 and n % 2 != 0:
        return (n*(F(n-1)+F(n-2)))//3

print(F(12))
