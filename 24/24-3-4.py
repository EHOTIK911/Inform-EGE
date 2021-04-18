f = open("24-3-4.txt")
line = 0
for s in f:
    if s.count("L") < s.count("K"):
        line+=1
print(line)
