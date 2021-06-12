def dell(n, m):
    return n % m == 0

A = 1
while True:
    Flag = False
    for x in range(1,100):
        if dell(18,x) <= (dell(54,x) <= dell(A,x)):
            Flag = True
            break
        if not Flag:
            print(A)
    A +=1

