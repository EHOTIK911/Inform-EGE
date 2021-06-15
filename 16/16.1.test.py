"""
F(1) = 1; G(1) = 1;
F(n) = F(n–1) – n·G(n–1), при n >=2
G(n) = F(n–1) + 2·G(n–1), при n >=2
Чему равно значение величины G(18)?

"""

def F(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) - n*G(n-1)
def G(n):
    if n == 1:
        return 1
    if n >=2:
        return F(n - 1) + 2*G(n - 1)
print(G(18))
