# test

for i in range(1, 1000):
    x = 0
    z = 0
    i = z
    a = 0
    b = 1
    if i == x:
        while x > 0:
            if x % 2 > 0:
                a += x % 8
            else:
                b *= x % 8
            x = x // 8
            if a == 2 and b == -24:
                print(z)
