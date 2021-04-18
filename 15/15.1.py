# Для какого наибольшего целого неотрицательного числа А выражение
# (x · y < 100) ∨ (y ≥ A) ∨ (x > A)
# тождественно истинно, т. е. принимает значение 1 при любых целых неотрицательных x и y?
def task15(x, y, A):
    return (x*y < 100) or (y >= A) or (x > A)

for A in range(1, 1000):
    Flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if task15(x, y, A) == False:
                Flag = False
                break
    if Flag == True:
        print(A)
