f = open("24_7.txt")
s = f.readline()
c = 0
cf = 0
for i in range(len(s)-2):
    if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] in "ACE" and s[i+1] in "ADF" and s[i+2] in "ABF":
        c += 1

print(c)
