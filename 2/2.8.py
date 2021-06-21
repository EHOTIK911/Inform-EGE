#(a ∨ ¬c) ∧ (b ∨ c)

print('a', 'b', 'c')

for a in range(2):
    for b in range(2):
        for c in range(2):
            if (a or (not c)) and (b or c) == 0:
                print(a,b,c)

