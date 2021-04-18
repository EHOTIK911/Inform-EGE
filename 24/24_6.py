f = open("24_6.txt")
s = f.readline()
c = 0
cf = 0
for i in range(len(s)):
    if s[i] in "ABEF":
        c += 1
        cf = max(cf , c)
    else:
        c = 0
print(cf)
