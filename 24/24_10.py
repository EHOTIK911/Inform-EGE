f = open("24_10.txt")
s = f.readline()
count = 1
count_final = 1
symb = ""
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
        if count > count_final:
            count_final = count
            symb = s[i]
    else:
        count = 1

print(count_final, symb)
