f = open("24-3-1.txt")
s = f.readline()
otvet = [s[0]]
otvet_final = []

for i in range(len(s)-1):
    if s[i] > s[i+1]:
        otvet.append(s[i+1])
        if len(otvet) > len(otvet_final):
            otvet_final = otvet
    else:
        otvet = [s[i+1]]
print("".join(otvet_final))

# ------- ANALOG -------
#
# f = open("24-3-1.txt")
# s = f.readline()
# otvet = s[0]
# otvet_final = []
#
# for i in range(len(s)-1):
#     if s[i] > s[i+1]:
#         otvet += s[i+1]
#         if len(otvet) > len(otvet_final):
#             otvet_final = otvet
#     else:
#         otvet = [s[i+1]]
# print(otvet_final)


