for i in range(650000, 1000000):
    for j in range(1,int(i)):
        count = 0
        for prost in range(2,int(j)):
            if j % prost == 0:
                count +=1


        if count == 0:
            for j2 in range(1,int(i)):
                count1 = 0
                for prost1 in range(2,int(j2)):
                    if j2 % prost1 == 0:
                        count1 +=1
                        if count == 0:
                            if j2 != j and (j+j2) % 10 == 4:
                                print(i, j+j2)

