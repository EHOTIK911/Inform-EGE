for x in range(1, 1000):
    L = 0
    M = 0
    xtrue = x
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
        if L == 5 and M == 8:
            print(xtrue)
