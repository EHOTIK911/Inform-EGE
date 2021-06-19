# + 1, сделай нечетное -- 1 в 25 и не содержит 24
# Вторая переводит число x в 2x + 1

def f(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    if x == 24:
        return 0
    K = f(start, x - 1)
    if x % 2 != 0:
        K += f(start, x // 2)
    return K

print(f(1, 25))
