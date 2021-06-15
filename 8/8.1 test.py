import itertools
# NOT WORK
a = list(itertools.product('НОБЕЛИЙ', repeat = 7))
count = 0
for x in a:
    if x.count('Н') == 1 and x.count('О')== 1 and x.count('Б')== 1 and x.count('Е')== 1 and x.count('Л')== 1 and x.count('И')== 1 and x.count('Й') == 1  :
        count +=1
print(count)
