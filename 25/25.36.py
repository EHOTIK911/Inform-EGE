'''
(№ 2905) (Б.С. Михлин) Напишите программу, которая ищет среди нечётных целых чисел,
принадлежащих числовому отрезку [248015; 251575] числа
(в порядке возрастания) с нечётным количеством делителей.
Для каждого такого числа выведите само число и делитель, квадрат которого равен этому числу.
ответ не правильный, но программа, по сути, работает правильно.
'''
a = []
count = 0
m = 0
for i in range(248015, 251575 + 1):
    b = []
    for j in range(1,int(i**0.5)+1):
        if i % j == 0:
            count += 1
        m = max(m,j)
    if (count % 2 != 0) and (m ** 2 == i):
        b.append(i)
        b.append(m)
    a.append(b)
print(a)

