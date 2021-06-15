f = open("24.14.txt")
s = f.readline()

count = 0
max = 0
for i in range(1, len(s) - 2):
    if (s[i] == "A" or s[i] == "C" or s[i] == "D") and (s[i+1] == "A" or s[i+1] == "С" or s[i+1] == "D"):
        count += 1
    if s[i+1] != "A" or s[i+1] != "С" or s[i+1] != "D":
        count = max
        count = 0
print(max)
