import itertools

a = list(itertools.product('ВИШНЯ', repeat = 6))

count = 0

for x in a:
    if x.count('В') < 2 and (x[0] != 'Ш' and x[5] != 'И' and x[5] != 'Я'):
        count +=1
print(count)
