'''
1. Прибавить 1
2. Прибавить 3
7 преобразуют в число 20
'''
def f(start,x):
    if x < start:
        return 0
    if x == start:
        return 1
    k = f(start, x - 1)
    k += f(start, x - 3)
    return k
print(f(7,20))
