"""
(№ 3982) Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000],
которые можно представить в виде N = 2**m•7**n, где m – нечётное число, n – чётное число.
В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n.
"""

a = []

for i in range(100000000, 300000000+1):
    b = []
    for m in range(1,30000):
        if m % 2 != 0:
            for n in range(1,30000):
                if n % 2 == 0:
                    if i == (2**m)*(7**n):
                        print(i, m+n)
