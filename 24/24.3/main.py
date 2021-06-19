'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов Y.
Хотя бы один символ Y находится в последовательности.

Для выполнения этого задания следует написать программу.
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
f = open("24_demo.txt")
s = f.readline()
count = 0
m = 0
for i in range(len(s) - 1):
    if s[i] == "Y" and s[i + 1] == "Y":
        count +=1
        m = max(m, count)
    else:
        count = 1
print(m)
