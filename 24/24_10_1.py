f = open("24_10.txt")
s = f.readline()

count = 1
count_final = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count +=1
        count_final = max(count_final, count)
    else:
        count = 1
print(count_final)
