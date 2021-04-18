f = open("24_8.txt")
s = f.readline()
c = 0
cf = 0
for i in range(len(s) - 2):
    b = set(s[i:i+3])
    if len(b) == 3:
        c +=1

print(c)

