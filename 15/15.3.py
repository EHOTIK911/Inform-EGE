# НЕ РАБОТАЕТ
"""
Элементами множеств А, P, Q являются натуральные числа, причём P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}, Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}.

Известно, что выражение



( (x ∈ P) → (x ∈ A)) V ( not (x ∈ A) → (not (x ∈ Q)))



истинно (то есть принимает значение 1) при любом значении переменной x. Определите наименьшее возможное количество элементов в множестве A.
"""
P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
def task15(x,A):
    return (((x in P) <= (x in A)) or ((not(x in A)) <= (not(x in Q))))

for A in range(1,1000):
    Flag = True
    for x in range(1,1000):
        if task15(x, A) == False:
            Flag = False
            break
    if Flag == True:
        print(A)

