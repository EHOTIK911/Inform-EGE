'''
Вася составляет 4-буквенные коды из букв К, Р, О, Й.
Каждую букву нужно использовать ровно 1 раз, при этом код не может начинаться с буквы Й
и не может содержать сочетания ОЙ.
Сколько различных кодов может составить Вася?
'''
import itertools

a = list(itertools.product('КРОЙ', repeat = 4))
count = 0
for x in a:
    if (x[0] != 'Й') and x.count('К')== 1 and (x.count('Р') == 1) and (x.count('О') == 1) and (x.count('Й') == 1):
        count +=1
        print(x)
print(count)
