import itertools

a = list(itertools.product("ИОУ", repeat = 5))
count = 0
for x in a:
    print(a, end ="/n")
    count+=1
print(count)
