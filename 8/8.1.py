#(А.Н. Носкин) Петя составляет семибуквенные слова перестановкой букв слова ТРАТАТА.
# Сколько всего различных слов может составить Петя?
# NOT WORK
import itertools

a = list(itertools.product("ТРАТАТА", repeat= 7))
count = 0
for x in a:
    x.count("T") == 3
