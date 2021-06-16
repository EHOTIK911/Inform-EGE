"""
Игорь составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
В качестве кодовых слов Игорь использует 5-буквенные слова, в которых есть только буквы П, И, Р,
причём буква П появляется ровно 1 раз. Каждая из других допустимых букв может встречаться
в кодовом слове любое количество раз или не встречаться совсем.
Сколько различных кодовых слов может использовать Игорь?
"""

import itertools

a = list(itertools.product("ПИР", repeat = 5))
count = 0
for x in a:
    if x.count("П") == 1:
        count += 1
print(count)
