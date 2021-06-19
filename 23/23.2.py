# + 1 , + 5 -- из 2 в 16

def f(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    K = f(start, x - 1)
    K += f(start, x - 5)
    return K

print(f(2, 16))
