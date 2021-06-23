f = open('24.txt')
s = f.readline()
count = 0
m = 0
for i in range(len(s)):
    if s[i] == '1' or s[i] == '2' or s[i] == '3':
        count += 1
        m = max(m,count)
    else:
        count = 0
print(m)
