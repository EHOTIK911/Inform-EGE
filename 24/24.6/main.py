'''
Текстовый файл состоит не более чем из 106 символов L, D и R.
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

Для выполнения этого задания следует написать программу.
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
f =open("zadanie24_2.txt")
s = f.readline()

count = 0
m = 0
for i in range(len(s) - 1):
    if s[i] != s [i + 1]:
        count +=1
        m = max(m, count)
    else:
        count = 1
print(m)
