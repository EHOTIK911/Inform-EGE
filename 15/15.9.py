'''
Укажите наименьшее целое значение А, при котором выражение
( – 2y + x < A) ∨ (x > 8) ∨ (y > 100)

истинно для любых целых положительных значений x и y.
'''

def task15(x,y,a):
    return (((-2)*y + x) < a) or (x > 8) or (y > 100)

for a in range(1,1000):
    Flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            if task15(x,y,a) == False:
                Flag = False
                break
    if Flag:
        print(a)
