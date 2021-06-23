for d in range(1,1000):
    n = 2
    s = 0
    dtrue = d
    while s <= 365:
        s = s + d
        n = n + 5
    if n == 67:
        print(dtrue)
