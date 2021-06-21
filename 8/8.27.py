def CheckRepeat(n):

   s = str(n)

   for i in s:

       c = s.count(i)

       if c > 1:

           return False

   return True

def CheckParity(n):

   s = str(n)

   for i in range(0, len(s)-1):

       if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0 or int(s[i]) % 2 == 1 and int(s[i + 1]) % 2 == 1:

           return False

   return True

count = 0

for i in range(10000, 99999+1):

   if i % 5 == 0 and Pov(i) and Chet(i):

       count += 1

print(count)
