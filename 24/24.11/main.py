'''
В текстовом файле k7.txt находится цепочка из символов латинского алфавита A, B, C длиной не более 106 символов.
Найдите длину самой длинной подцепочки, состоящей из символов C.
'''

f = open('k7.txt')
s = f.readline()
count = 0
m = 0
for x in range(len(s)-1):
    if s[x] == 'C' and s[x+1] == 'C':
        count +=1
        m = max(m,count)
    else:
        count = 1
print(m)
