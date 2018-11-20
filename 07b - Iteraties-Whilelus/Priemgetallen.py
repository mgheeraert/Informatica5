#invoer
getal = int(input('geef getal: '))
antwoord =''
a = 2
b = 1

#berekening
while a < getal:
    if (getal % a) == 0:
        b = 0
        antwoord = '{} is geen priemgetal'.format(getal)
    a += 1
print(antwoord)
if b and getal != 1:
    print('{} is een priemgetal'.format(getal))
elif getal == 1:
    print('1 is geen priemgetal')