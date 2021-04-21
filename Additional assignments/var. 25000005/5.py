"""
Задание 5 (№206).

Автомат обрабатывает трёхзначное натуральное число N по следующему алгоритму.

1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные двузначные числа (числа не могут начинаться с нуля).

2. На экран выводится разность полученных двузначных чисел.

Пример. Дано число N = 351. Алгоритм работает следующим образом.

1. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13.

2. На экран выводится разность 53 – 13 = 40.

Чему равно количество чисел N на отрезке [800; 900], в результате обработки которых на экране автомата появится число 30?

"""

def f(n):
    n1, n2, n3 = sorted([int(a) for a in str(n)])
    return n3*10 + n2 - (n1*10 + n2)

counter = 0
for i in range(800,901):
    if f(i) == 30:
        counter += 1
print(counter)

#Ответ: 9