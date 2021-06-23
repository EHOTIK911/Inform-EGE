f = open('24.txt')
s = f.readline()
count = 0
m = 0
for i in range(len(s)-3):
    if not (s[i] == 'X' and s[i+1] == 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y'):
        count +=1
        m = max(m,count)
    else:
        count = 3
print(m)
