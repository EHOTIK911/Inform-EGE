# +2 +4 -- из 2 в 10


def f(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    K = f(start, x - 2)
    K += f(start, x - 4)
    return K

print(f(2, 10))
