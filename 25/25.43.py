
n = 452022
count_n = 0
minM = 999999
maxM = 0
while count_n != 5:
    M = 0
    for i in range(2,n):
        if n % i == 0:
            minM = min(minM, i)
            maxM = max(maxM,i)
            break

    M = maxM + minM

    if M % 7 == 3:
        count_n +=1
        print(n, M)
    n +=1
