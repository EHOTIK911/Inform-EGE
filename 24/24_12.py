f = open("24_12.txt")
line = 0
for s in f:
    if s.count("K") > s.count("U"):
        line +=1
print(line)
