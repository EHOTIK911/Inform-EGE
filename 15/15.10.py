'''
(№ 4195) (С. Скопинцева) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n
делится без остатка на натуральное число m».
Для какого наибольшего натурального числа А формула
¬ (ДЕЛ(x, 16) ≡ ДЕЛ(x, 24)) → ДЕЛ(x, A)

тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
'''

def dell(n, m):
    return n % m == 0



for a in range(1,1000):
    Flag = False
    for x in range(1,1000):
        if not(dell(x,16) == dell(x,24)) <= dell(x, a):
            Flag = True
        if Flag:

            print(a)
