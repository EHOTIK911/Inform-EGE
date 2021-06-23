'''
(№ 3586) Сколько единиц в двоичной записи числа 8415 – 4162 + 2543 – 25
'''

def calc(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x = x // b
    return s[::-1]

x = 8**415 - 4**162 + 2**543 - 25

x = calc(x,10,2)
print(x.count('1'))
