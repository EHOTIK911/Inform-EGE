f = open("24_13.txt")
s = f.readline()
slovar = {}
for i in range(len(s)):
    if s[i] == "X":
        if slovar.get(s[i+1], 0) != 0:
            slovar[s[i+1]] +=1
        else:
            slovar[s[i+1]] = 1
max_final = [0 , ""]
for key in slovar.keys():
    if slovar[key] > max_final[0]:
        max_final[0] = slovar[key]
        max_final[1] = key
print(max_final)
