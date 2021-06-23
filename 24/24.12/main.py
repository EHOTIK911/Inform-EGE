f = open('24 (2).txt')
s = f.readline()
m = 0
count = 0
for i in range(len(s) + 1):
    if s[i] != '0':
        count += 1
        m = max(m,count)

    else:
        count = 0

print(m)
