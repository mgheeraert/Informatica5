#invoer
a = float(input('geef a: '))
b = float(input('geef b: '))

#berekening
ll = abs(abs(a)- abs(b))
rl = abs(a - b)

#uitvoer
resultaat = ('{:.4f}  ≤  {:.4f}' .format(ll, rl))

print(resultaat)