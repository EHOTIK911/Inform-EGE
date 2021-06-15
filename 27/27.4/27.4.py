f = open("27-26a.txt", "r")
n = int(f.readline())




for i in range(n):
    a = 10
    b = 16
    def calc(x, a, b):
        x = int(str(x), a)
        s = ''
        while x > 0:
            s += str(x % b)
            x = x // b
        return s[::-1]
    x, y = map(int, f.readline().split())
    print(x)
