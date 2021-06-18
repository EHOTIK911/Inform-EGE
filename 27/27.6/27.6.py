f = open("27985_B.txt")
l = open("27985_B1.txt")
s = int(f.readline())
max = 0

m = []
for i in range(s):
    m.append(int(f.readline()))


for i in range(s):
    x1 = m[i]
    for j in range(s-1):
        x2 = m[j]
        if (x1*x2 % 14 == 0) and (x1*x2 > max):
            max = x1*x2
            print(max)
print(max)
