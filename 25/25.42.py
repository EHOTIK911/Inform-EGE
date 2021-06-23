'''
задание с предбанника
'''

n = 650001
count_n = 0

while count_n !=6:
    M = 0
    for i in range(2, n):
        if n % i == 0:
            M += i
    if M % 17 == 0:
        count_n +=1
        print(n, M//17)
    n +=1
