'''
Пётр составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
В качестве кодовых слов Пётр использует все пятибуквенные слова в алфавите {A, B, C, D, E, F},
удовлетворяющие такому условию: кодовое слово не может начинаться с буквы F и заканчиваться буквой A.
Сколько различных кодовых слов может использовать Пётр?
'''
import itertools

a = list(itertools.product("ABCDEF", repeat = 5))
count = 0
for x in a:
    if x[0] != "F" and x[4] != "A":
        count += 1
print(count)
