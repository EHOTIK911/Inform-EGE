# + 1 , * 2 , + 3 -- 2 in 14 и не содержит 5 и 10

def f(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    if x == 5 or x == 10:
        return 0
    K = f(start, x - 1)
    if x % 2 == 0:
        K += f(start, x // 2)
    K += f(start, x - 3)
    return K

print(f(2, 14))
