"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457;174505], числа,
имеющие ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа
запишите эти два делителя в два соседних столбца на экране с новой строки в порядке возрастания произведения этих двух делителей.
Делители в строке также должны следовать в порядке возрастания.
"""

a = []

for i in range(174457, 174505 + 1):
    b = []
    if i**0.5 == int(i**0.5):
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            b.append(j)
            b.append(i//j)
        if len(b) > 2:
            break
    if len(b) == 2:
        a.append(b)
print(a)
