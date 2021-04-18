#Не работает
"""
На числовой прямой даны два отрезка: P = [2, 10] и Q = [6, 14].

Какова наибольшая возможная длина интервала A, что формула



((x ∈ А) → (x ∈ P)) ∨ (x ∈ Q)



тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
"""
for P in range(2,9):
    for Q in range (6,13):
        def task15(x, A):
            return int(((x in A) <= (x in P)) or (x in Q))

        for A in range (1,1000):
            Flag = True
            for x in range (1, 1000):
                if task15(x, A) == False:
                    Flag = False
                    break
            print(A)

