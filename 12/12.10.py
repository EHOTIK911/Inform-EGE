'''
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 247 идущих подряд цифр 5? В ответе запишите полученную строку.
НАЧАЛО
ПОКА нашлось (222) ИЛИ нашлось (555)
  ЕСЛИ нашлось (222)
    ТО заменить (222, 5)
    ИНАЧЕ заменить (555, 2)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
'''
a = '5' * 247

while ('222' in a) or ('555' in a):
    a = a.replace('222', '5', 1)
else:
    a = a.replace('555', '2', 1)
print(a)

'''

'''
