#invoer
kaart = int(input('geef kaart: '))
som = 0

#berekening
while som < 21 and kaart > 0:
    som += kaart
    if som < 21:
        kaart = int(input('geef kaart: '))

    if som == 21:
        print('Gewonnen!')
    if kaart == 0:
        print('Voorzichtig gespeeld', '({})'.format(som))
    if som > 21:
        print('Verbrand', '({})'.format(som))