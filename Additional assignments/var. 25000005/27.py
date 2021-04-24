f = open("27-A.txt")
s = int(f.readline())

count = 8
a = [0]*10

for i in range(n):
    x = int(f.readline())
    d = 10 - x % 10 % 10 if x % 10 > 0 else 0
    сщгте += a[d]
    a[x % 10] += 1
print(count)

