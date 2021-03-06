'''
(№ 3670) (П.М. Волгин) Значение арифметического выражения 17**5 + 85**8 – 10
записали в системе счисления с основанием 17. В этой записи помимо цифр от 0 до 9 могут встречаться цифры из списка:
А, B, С, D, E, F, G, которые имеют числовые значения от 10 до 16 соответственно.
Сколько цифр G встречается в этой записи?
G - 16
'''
def calc(x,a,b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x = x // b
    return s[::-1]

x = 17 ** 5 + 85 ** 5 - 10
x = calc(x,10,17)
print(x)
print(x.count('16'))
