'''
Сколько единиц в двоичной записи числа 8**1023 + 2**1024 – 3
'''
def calc(x,a,b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x = x // b
    return s[::-1]

x = 8**1023 + 2**1024 - 3
x = calc(x, 10, 2)
print(x)

# 1024
