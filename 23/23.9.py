def f(start,x):
    if x < start:
        return 0
    if x == start:
        return 1
    k = f(start, x - 2)
    k += f(start, x - 5)
    return k

print(f(2,23))
