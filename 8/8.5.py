"""
Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой, можно составить из букв М, Е, Т, Р, О?
Каждая буква может входить в слово несколько раз.
Слова не обязательно должны быть осмысленными словами русского языка.
"""


import itertools

a = list(itertools.product("МЕТРО", repeat = 4))

count = 0

for x in a:
    if (x[0] == 'М' or x[0] == 'Т' or x[0] == 'Р') and (x[3] == "Е" or x[3] == "О"):
        count +=1
        print(x)
print(count)
