"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [2422000; 2422080], простые числа.
Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку.
"""
for x in range(2422000, 2422080+1):
    count = 0
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            count +=1

    if count == 0:
        print(x-2422000+1, x)

