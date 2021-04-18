f = open("24_11.txt")
s = f.readline()

count = [s[0]]
count_final = []

for i in range(len(s) - 1):
    if s[i] < s[i+1]:
        count.append(s[i+1])
        if len(count) > len(count_final):
            count_final = count

    else:
        count = [s[i+1]]
print("".join(count_final))
