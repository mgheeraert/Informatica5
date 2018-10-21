from random import random, randint, seed

#invoer
a = float(input('geef a: '))
b = float(input('geef b: '))

#berekening
getal_1 = (10**0)*a
getal_2 = (10**0)*b
getal_A = getal_1 + getal_2
getal_3 = (10**1)*a
getal_4 = (10**1)*b
getal_B = getal_3 + getal_4
getal_5 = (10**2)*a
getal_6 = (10**2)*b
getal_C = getal_5 + getal_6
getal_7 = (10**3)*a
getal_8 = (10**3)*b
getal_D = getal_7 + getal_8
getal_9 = (10**4)*a
getal_10 = (10**4)*b
getal_E = getal_9 + getal_10
#uitvoer
print('{:>6.0f} + {:<6.0f} = {:<6.0f}' .format(getal_1, getal_2, getal_A))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}' .format(getal_3, getal_4, getal_B))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}' .format(getal_5, getal_6, getal_C))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}' .format(getal_7, getal_8, getal_D))
print('{:>6.0f} + {:<6.0f} = {:<6.0f}' .format(getal_9, getal_10, getal_E))
