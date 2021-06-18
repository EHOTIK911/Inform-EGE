'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [568023;569230], число,
имеющее максимальное количество различных натуральных делителей, если таких чисел несколько — найдите минимальное из них.
Выведите на экран количество делителей такого числа и само число.
'''
a = []
for i in range(568023, 569230 + 1):
    count = 0
    max_count = 0
    final_count = 0
    b = []
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
        if count > max_count:
            max_count = count
    if final_count <= max_count:
        final_count = max_count
        b.append(final_count)
        b.append(i)
    print(b)

