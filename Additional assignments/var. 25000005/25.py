for i in range(228224, 531135 + 1):
    d = 3
    count, m = 0,0
    while d*d*d <= i:
        if i % (d*d*d) == 0:
            count += 1
            m = d*d*d
        d += 2
    if count > 3:
        print(count, i)
