'''
НАЧАЛО
ПОКА нашлось(11)
  заменить(112, 4)
  заменить(113, 2)
  заменить(42, 3)
  заменить(43, 1)
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой программы к строке вида 1…13…32…2,
состоящей из 170 единиц, 100 троек и 7 двоек?
'''

a = "1" * 170 + '3'* 100 + "2" * 7

while '11' in a:
    a = a.replace('112',"4", 1)
    a = a.replace('113',"2", 1)
    a = a.replace('42',"3", 1)
    a = a.replace('41',"1", 1)
print(a)
