aantal = int(input('aantal:'))
grootste = int(input('getal: '))
som = grootste

for i in range (aantal - 1):
    getal = int(input('getal: '))
    som += getal
    if(getal) > grootste:
        grootste = getal

print('het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootste, som/aantal))