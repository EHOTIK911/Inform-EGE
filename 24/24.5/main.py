'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки вида XYZXYZXYZ...
(составленной из фрагментов XYZ, последний фрагмент может быть неполным).

Для выполнения этого задания следует написать программу.
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
f = open ("C:\Users\Petr\PycharmProjects\pythonProject\Inform EGE\24\24.5\24_demo.txt")
s = f.readline()

count = 0
m = 0

for i in range(len(s) - 2):
    if s[i] == "X" and s[i + 1] == "Y" and s[i + 2] == "Z":
        count +=1
        m = max(m, count)
    else:
        count =1
print(m)
