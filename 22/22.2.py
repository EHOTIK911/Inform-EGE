for x in range(101,1000):
    L = x - 20
    M = x + 15
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 35:
        print(x)

