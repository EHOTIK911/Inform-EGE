"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [201455; 201470], числа,
имеющие ровно 4 различных натуральных делителя.
Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.
"""

a = []

for i in range(201455, 201470 + 1):
    b = []
    if i**(1/2) == int(i**(1/2)):
        continue
    for j in range(1, int(i**(1/2))+1):
        if (i % j == 0):
            b.append(j)
            b.append(i//j)
        if len(b) > 4:
            break
    if len(b) == 4:
        a.append(b)
print(a)