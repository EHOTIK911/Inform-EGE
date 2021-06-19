
f = open("24_demo.txt")
s = f.readline()
for i in range(1, len(s)+1):
    count = 0
    max_count = 0
    if s[i] != s[i+1]:
        count +=1
        if count > max_count:
            max_count = count
            print(max_count)


