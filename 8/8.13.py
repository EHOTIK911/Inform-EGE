'''
Максим составляет таблицу кодовых слов для передачи сообщений,
каждому возможному сообщению соответствует своё кодовое слово.
В качестве кодовых слов Максим использует четырёхбуквенные слова,
в которых есть только буквы A, B, C, D, E, F, X, причём буква X появляется ровно 1 раз.
Сколько различных кодовых слов может использовать Максим?
'''

import itertools

a = list(itertools.product("ABCDEFX", repeat = 4))

count = 0

for x in a:
    if x.count("X") == 1:
        count +=1
print(count)