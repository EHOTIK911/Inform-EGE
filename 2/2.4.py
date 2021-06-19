# (x ∧ y ∧¬z) ∨ (x ∧ y ∧ z) ∨ (x ∧¬y ∧¬z)

print('x', 'y', 'z')
for x in range (2):
    for y in range(2):
        for z in range(2):
            if (x and y and (not z)) or (x and y and z) or (x and (not y) and (not z)) == 1:
                print(x, y, z)
