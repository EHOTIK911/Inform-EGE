for x in range(1, 10000):
    a, b = 0, 1
    truex = x
    while x > 0:
        a = a + 1
        b = b * (x%100)
        x = x//100
    if a == 2 and b == 7:
        print(truex)
