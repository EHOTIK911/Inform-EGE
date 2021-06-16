'''
Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А.
Каждую букву нужно использовать ровно 1 раз, при этом Ь нельзя ставить
первым и нельзя ставить после гласной. Сколько различных кодов может составить Ольга?
'''

import itertools

a = list(itertools.product('ОЛЬГА', repeat = 5))

count = 0
for x in a:
    if (x.count('О') == 1 and x.count('Л') == 1 and x.count('Ь') == 1 and x.count('Г') == 1 and x.count('А') == 1) and (x[0] != "Ь") and not((x[0] == "О" or x[0] == "А") and x[1] == "Ь") and not((x[1] == "О" or x[1] == "А") and x[2] == "Ь") and not((x[2] == "О" or x[2] == "А") and x[3] == "Ь") and not((x[3] == "О" or x[3] == "А") and x[4] == "Ь"):
        count +=1

print(count)
