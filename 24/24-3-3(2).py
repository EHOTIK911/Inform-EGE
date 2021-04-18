f = open("24-3-3.txt")
s = f.readline()
otvet = s[0]
otvet_final = ""
for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        otvet = otvet + s[i+1]
        if len(otvet) > len(otvet_final):
            otvet_final = otvet
    else:
        otvet = s[i+1]
print(otvet_final)
print(len(s))
print(len(otvet_final))

