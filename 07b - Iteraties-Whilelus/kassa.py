#invoer
getal = 1
som = 0

#berekening
while getal > 0:
    getal = float(input('getal: '))
    som += getal

#uitvoer
print('De totale prijs is €', '{:.2f}'.format(som))