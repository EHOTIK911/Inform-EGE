n = 600001
count_n = 0
while count_n!= 6:
    F = 0
    for i in range(2,n):
        if n % i == 0 :
            F = n//i - i
            break
    if F != 0 and F % 7 == 0:

        count_n +=1
        print(n, F)

    n += 1
