'''
Левий составляет 5-буквенные коды из букв Л, Е, В, И, Й.
Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ЕИ.
Сколько различных кодов может составить Левий?
'''

import itertools

a = list(itertools.product('ЛЕВИЙ', repeat = 5))
count = 0
for x in a:
    if x[0] != "Й" and (x.count("Л") == 1 and x.count("Е") == 1 and x.count("В") == 1 and x.count("И") == 1 and x.count("Й") == 1) and not(x[0] == "Е" and x[1] == 'И') and not(x[1] == "Е" and x[2] == 'И') and not(x[2] == "Е" and x[3] == 'И') and not(x[3] == "Е" and x[4] == 'И'):
        count +=1
print(count)
