'''
(№ 3585) Сколько единиц в двоичной записи числа 8115 – 4123 + 2543 – 15
'''

def calc(x,a,b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x = x // b
    return s[::-1]

x = 8**115 - 4**123 + 2**543 - 15
x = calc(x,10,2)
print(x.count('1'))
