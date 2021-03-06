'''
(№ 4076) (В. Шелудько) Значение выражения 7**1003 + 6∙7**1104 – 3∙7**57 + 294 записали в системе счисления с основанием 7.
Найдите сумму цифр получившегося числа и запишите её в ответе в десятичной системе счисления
'''

def calc(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x = x//b
    return s[::-1]

x = 4**1503 + 3*(4**244) - 2*(4**1444) - 96
x = calc(x, 10, 4)
print(x)

# 3 * 298 + 2*4 = 902
