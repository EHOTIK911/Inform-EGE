def task15(x, A):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & A != 0))

for A in range(0,1000):
    Flag = True
    for x in range(0,1000):
        if task15(x, A) == 0:
            Flag = False
            break
    if Flag:
        print(A)
