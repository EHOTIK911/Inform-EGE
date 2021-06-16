'''
Вася составляет 5-буквенные слова, в которых есть только буквы З, И, М, А,
причём в каждом слове есть ровно одна гласная буква и она встречается ровно 1 раз.
Каждая из допустимых согласных букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
'''
import itertools

a = list(itertools.product("ЗИМА", repeat = 5))
count = 0
for x in a:
    if (x.count("И") == 1 and x.count("А") == 0) or (x.count("И") == 0 and x.count("А") == 1):
        count += 1
print(count)