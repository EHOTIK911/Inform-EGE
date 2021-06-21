for x in range(101,1000):
    L = x - 16
    M = x + 16
    xtrue = x
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    if M == 16:
        print(xtrue)
