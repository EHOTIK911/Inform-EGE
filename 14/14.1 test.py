def calc(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x = x // b
    return s[::-1]


# 9^20 + 3^60 – 15

x = (9 ** 20) + (3 ** 60) - 15
x = calc(x, 10, 3 )
print(x.count('2'))
