"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245690;245756] простые числа.
Выведите на экран все найденные простые числа в порядке возрастания, слева от каждого числа выведите его порядковый номер в последовательности.
Каждая пара чисел должна быть выведена в отдельной строке.
"""

for x in range(245690, 245756+1):
    count = 0
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            count += 1
    if count == 0:
        print(x-245690+1, x)
