def bereken_prijs(zin):
    bedrag = zin[-5:-2]
    prijs = 0
    for i in range(0, len(zin) - 6):
        if len(zin) > 0:
            prijs += bedrag * (len(zin)-6)
        else:
            prijs += 0

    return prijs

print(bereken_prijs('I spent my last money on this billboard. Please give me a job.<2.68>'))
