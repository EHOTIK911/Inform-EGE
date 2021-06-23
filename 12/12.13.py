a = '2' * 30 + '1' * 30 + '3' * 30 

while '21' in a or '23' in a:
    if '21' in a:
        a = a.replace('21','11',1)
    else:
        a = a.replace('23','21',1)
print(a.count('1'))
