#test
for x in range(1,1000):
    i = 0
    x = i
    a = 0
    b = 1
    while x > 0:
        if x%2 > 0:
            a += x%8
        else:
            b *= x%8
        x = x//8
    if a == 2 and b == -24:
        print(i)
