# + 1, * 2 -- 3 в 62, содержит 14 и не содержит 59

def f(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    if x == 59:
        return 0
    K = f(start, x - 1)
    if x % 2 == 0:
        K += f (start, x//2)
    return K
print(f(3,14) * f(14, 62))
