def F(n):
  print("*")
  if n > 0:
    print("*")
    G(n - 1)
def G(n):
  print("*")
  if n > 1:
    F(n - 2)
print(F(12))


