'''
NOT WORK
Сколько существует шестизначных чисел, делящихся на 5,
в которых каждая цифра может встречаться только один раз,
при этом никакие две чётные и две нечётные цифры не стоят рядом.
'''
import itertools

a = list(itertools.product("0123456789", repeat = 6))
count = 0
for x in a:
    if x[5] == 5 or x[5] == 0:
        count+=1
        print(a)
print(count)
