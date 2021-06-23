# (х → y) ∨ ¬( w → z)
print('x', 'y', 'w', 'z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x <= y) or (not(w<=z))) == False:
                    print(x,y,w,z)
