'''
Вася составляет 6-буквенные слова из букв К, О, Т.
Причем буква К используется в каждом слове ровно 1 раз.
Остальные буквы могут быть использованы любое количество раз, в том числе совсем отсутствовать.
Сколько слов может составить Вася? Словом называется любая буквенная комбинация, не обязательно осмысленное слово русского языка.
'''
import itertools

a = list(itertools.product("КОТ", repeat = 6))

count = 0
for x in a:
    if x.count("К") == 1:
        count +=1
print(count)
