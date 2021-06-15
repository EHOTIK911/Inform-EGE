

with open("27-A.txt", "r") as f: # Открываем файл для чтения
    n = int(f.readline()) # считываем превую строчку
    sum = 0 # Создаем переменную для суммы
    min_diff = 10001 # Создаем переменную с минимальной разницей в зависимости от того, какое максимальное число строк может быть,
                     # к примеру возмем 10000(делаем +1 чтобы в перебоне не делать +1, этого можно и не делать)
    for i in range(n):
        x,y = map(int, f.readline().split())
        sup = s + max(x, y) # находим сумму с максимальный x или у
        diff = abs(x - y) # Находим разницу
        if diff % 3 != 0:
            min_diff = main(diff, min_diff)
    if s % 3 != 0: # если остаток при делениие на ... допустим 3 не равняется нулю, то выводим сумму
        print(sup)
    else:
        print(s - min_diff)
"""
СПРАВКА
-------------------
функция map()
Встроенная в Python функция map() используется для применения функции к каждому элементу итерируемого объекта (например, списка или словаря)
и возврата нового итератора для получения результатов. Функция map() возвращает объект map (итератор),
который мы можем использовать в других частях нашей программы.
Также мы можем передать объект map в функцию list() или другой тип последовательности для создания итерируемого объекта.
-------------------
функция abs()
Возвращает модуль числа
-------------------
"""

