def task15(x,a):
    return (x & 57 != 0) and (x & 38 != 0) or (x & 9 == 0) or (x & a == 0)

for a in range(1,1000):
    Flag = True
    for x in range(1,1000):
        if task15(x,a) == False:
            Flag = False
            break
    if Flag:
        print(a)
