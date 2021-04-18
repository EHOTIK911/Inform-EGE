def task15(x,A):
    return (x & 49 != 0) <= ((x & 41 == 0) <= (x & A != 0))

for A in range (1, 1000):
    Flag = True
    for x in range(1, 1000):
        if task15(x, A) == False:
            Flag = False
            break
    if Flag:
        print(A)

