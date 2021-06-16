'''
Рассматриваются символьные последовательности длины 5 в шестибуквенном алфавите {У, Ч, Е, Н, И, К}.
Сколько существует таких последовательностей, которые начинаются с буквы У и заканчиваются буквой К?
'''

import itertools

a = list(itertools.product("УЧЕНИК", repeat = 5))

count = 0

for x in a:
    if x[0] =="У" and x[4] == 'К':
        count += 1
print(count)
