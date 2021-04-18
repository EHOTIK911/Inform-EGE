f = open("24_1.txt")
s = f.readline()
i = 0
c = 0
cf = 0

while  i < len(s):
    if s[i:i+4] == "LDRL":
        c += 4
        cf = max(cf,c)
        i += 4
    elif s[i-1:i+3] == "LDRL":
        c = 4
        cf = max(cf,c)
        i += 4
    else:
        c = 0
        i +=1
print(cf)
