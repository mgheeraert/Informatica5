#invoer
stijn = int(input('snelheid stijn: '))
kaat = int(input('snelheid kaat: '))
afstand = int(input('de afstand: '))
seconden = 1

#berekening
while afstand  > (kaat + stijn):
     seconden += 1
     afstand = afstand - kaat - stijn


#uitvoer
print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'. format(seconden))