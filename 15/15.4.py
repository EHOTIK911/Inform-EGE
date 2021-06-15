# (3y + 2x ≠ 130) ∨ (3x > A) ∨ (2y > A)

def task15(x, y, a):
    return ((3*y + 2*x) != 130) or (3*x > a) or (2*y > a)

for a in range(1,100):
    Flag = True
    for x in range(1,100):
        for y in range(1,100):
            if task15(x, y ,a) == False:
                Flag = False
                break
    if Flag:
        print(a)
