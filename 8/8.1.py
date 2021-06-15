#(А.Н. Носкин) Петя составляет семибуквенные слова перестановкой букв слова ТРАТАТА.
# Сколько всего различных слов может составить Петя?

import itertools

a = list(itertools.product("ТРАТАТА", repeat= 7))
count = 0
for x in a:
    if x.count("Т") == 1 and x.count("Р") == 1 and x.count("А") == 1 and x.count("Т") == 1 and x.count("А") == 1 and x.count("Т") == 1 and x.count("А") == 1:
        count +=1
print(7*6*5*4*3*2*1)

