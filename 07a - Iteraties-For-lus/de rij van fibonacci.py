#invoer
nde_getal = int(input('Het hoeveelste getal uit de rij van Fibonacci?: '))
getal_1, getal_2 = 1, 1

#berekening
if nde_getal > 2:
    for _ in range(3, nde_getal + 1):
        nieuw_getal = getal_1 + getal_2
        getal_1 = getal_2
        getal_2 = nieuw_getal
    print(nieuw_getal)
elif nde_getal == 1 or nde_getal == 2:
    print('1')

