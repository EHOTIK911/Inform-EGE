"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [312614;312651], числа,
имеющие ровно шесть различных натуральных делителей. Для каждого найденного числа запишите эти шесть
делителей в шесть соседних столбцов на экране с новой строки.
Делители в строке должны следовать в порядке возрастания.
"""
a = []

for i in range(312614, 312651 + 1):
    b = []
    if i**(1/2) == int(i**(1/2)):
        continue
    for j in range(1, int(i**(1/2)) + 1):
        if (i % j == 0):
            b.append(j)
            b.append(i//j)
        if len(b) > 6:
            break
    if len(b) == 6:
        a.append(b)
print(a)