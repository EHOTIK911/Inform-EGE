def calc(x,a,b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str( x % b)
        x = x //b
    return s[::-1]

x = 7*(512**120) - 6 * (64**100) + 8**210 - 255

x = calc(x,10,8)
print(x.count('0'))
