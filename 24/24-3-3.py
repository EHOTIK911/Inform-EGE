f = open("24-3-1.txt")
s = f.readline()
count = 1
cf = 1
symb = ""
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        count += 1
        if count > cf :
            cf = count
            symb = s[i]

    else:
        count = 1

print(symb , cf)
