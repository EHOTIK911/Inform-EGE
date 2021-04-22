#test
def output(n):
    answ = 0
    i = 3
    cube = i * i * i
    maxcube = cube
    while cube <= n:
        if n % cube == 0:
            answ += 1
            maxcube = cube
    i += 2
    cube = i * i * i
    print(answ, maxcube)

def cnt(n):
    answ = 0
    i = 3
    cube = i * i * i
    while cube <= n:
        if n % cube == 0:
            answ += 1
        i += 2
        cube = i * i * i
    return answ
k = 0
for n in range(228224, 531135 + 1):
    if cnt(n) >= 4:
    output(n)
