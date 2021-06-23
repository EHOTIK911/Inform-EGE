def f(start,x):
    if x < start:
        return 0
    if x == start:
        return 1
    if x == 21:
        return 0
    k = f(start, x - 1)
    if x % 3 == 0:
        k +=f(start, x // 3)
    if x % 4 == 0:
        k += f(start, x // 4)
    return k

print(f(2,16) * f(16,60))
