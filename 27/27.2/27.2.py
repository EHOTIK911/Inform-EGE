"""
Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число так, чтобы
сумма всех выбранных чисел не делилась на 3 и при этом была максимально возможной. Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число — максимально возможную сумму, соответствующую условиям задачи.
Входные данные.
Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество пар N(1 ≤ N ≤ 100000). Каждая из
следующих N строк содержит два натуральных числа, не превышающих 10 000.
27A-1-1.txt 27B-1-1.txt
Пример организации исходных данных во входном файле:
6
1 3
5 12
6 9
5 4
3 3
1 1
Для указанных входных данных значением искомой суммы должно быть число 32.
В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.
Предупреждение: для обработки файла B не следует использовать переборный алгоритм, вычисляющий сумму для всех возможных
вариантов, поскольку написанная по такому алгоритму программа будет выполняться слишком долго.

"""
f = open("27B-1-1.txt")
n = int(f.readline())
sum = 0
min_diff = 1000001
for i in range(n):
    a, b = map(int,f.readline().split())
    sum += max(a,b)
    if abs(a-b) < min_diff and abs(a-b) % 3 !=0:
        min_diff = abs(a-b)
if sum % 3 == 0:
    print(sum - min_diff)
else:
    print(sum)
