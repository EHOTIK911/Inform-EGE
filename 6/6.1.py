for s in range(1,1000):
    n = 1
    strue = s
    while s < 47:
        s = s + 4
        n = n * 2
    if n == 64:
        print(strue)
