'''
Укажите наибольшее целое значение А, при котором выражение
(y + 5x ≠ 80) ∨ (3x > A) ∨ (y > A)

истинно для любых целых положительных значений x и y.

'''
def task15(x,y,a):
    return ((y + 5*x) != 80) or (3*x > a) or (y > a)

for a in range(1,1000):
    Flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            if task15(x,y,a) == False:
                Flag = False
                break
    if Flag:
        print(a)
