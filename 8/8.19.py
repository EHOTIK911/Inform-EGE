'''
Михаил составляет 5-буквенные коды. В кодах разрешается использовать только буквы А, Б, В, Г, Д,
при этом код не может начинаться с гласной и не может содержать двух одинаковых букв подряд.
Сколько различных кодов может составить Михаил?
'''

import itertools

a = list(itertools.product("АБВГД", repeat = 5))

count = 0

for x in a:
    if x[0] != "А" and x[0] != x[1] and x[1] != x[2] and x[2] != x[3] and x[3] != x[4]:
        count +=1
print(count)
