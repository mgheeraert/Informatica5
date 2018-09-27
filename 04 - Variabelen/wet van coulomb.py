#invoer
q1 = 2.0 * (10**-6)
q2 = 1.0 * (10**-6)
k = 8.99 * (10**9)
r = float(input('geef r: '))

r = r * (10 ** -2)

#berekening
wet_van_coulomb = k * (q1 * q2) / (r**2)


print(wet_van_coulomb)
