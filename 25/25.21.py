"""
(№ 2926) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
отрезку [209834; 209857], числа, имеющие ровно 4 различных делителя.
Выведите для каждого найденного числа два наибольших делителя в порядке возрастания.

"""

a = []

for i in range(209834, 209857 + 1):
    b = []
    if i ** 0.5 == int(i**0.5):
        continue

    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            b.append(j)
            b.append(i//j)
        if len(b) > 4:
            break
    if len(b) == 4:
        a.append(b)
print(a)

"""
104917 209834
941 209843
41969 209845
1213 209849
"""
