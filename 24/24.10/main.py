f = open("k8-10.txt")
s = f.readline()
count = 0
m = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count +=1
        m = max(m,count)
    else:
        count = 1

print(m)
