# (¬x ∧ y ∧ z) ∨ (¬x ∧ y ∧ ¬z) ∨ (¬x ∧ ¬y ∧ ¬z)
print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not x) and y and z) or ((not x) and y and (not z)) or ((not x) and (not y) and (not z)):
                print(z,y,z)
print(bin(171))
print(1 + 8 + 128)
print(int("101011", 2))
"""
130 - 10000010
      10001001 (1 + 8 + 128) 
      10101100
"""
