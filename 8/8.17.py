'''
Олег составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
В качестве кодовых слов Олег использует 4-буквенные слова, в которых есть только буквы A, B, C, D, E, X, Z,
причём буквы X и Z встречаются только на двух первых позициях,
а буквы A, B, C, D, E — только на двух последних. Сколько различных кодовых слов может использовать Олег?
'''
import itertools

a = list(itertools.product("ABCDEXZ", repeat = 4))
count = 0
for x in a:
    if (x[0] == "X" or x[0] == "Z") and (x[1] == "X" or x[1] == "Z") and x[2] != "X" and x[2] != "Z" and x[3] != "X" and x[3] != "Z":
        count +=1
print(count)