def kleur_toevoegen(kleuren, nieuwe_kleur):
    hoeveelheid = kleuren
    rood = kleuren[0]
    groen = kleuren[1]
    blauw = kleuren[2]

    for i in range(0, len(kleuren)):
        if nieuwe_kleur == 'blauw':
            hoeveelheid.pop(2)
            hoeveelheid.insert(2,blauw + 1 )
        elif nieuwe_kleur == 'rood':
            hoeveelheid.pop(0)
            hoeveelheid.insert(0, rood + 1)

        elif nieuwe_kleur == 'groen':
            hoeveelheid.pop(1)
            hoeveelheid.insert(1, groen + 1)

    return hoeveelheid

def is_wit(kleuren):
    antwoord = False

    if kleuren[0] == kleuren[1] and kleuren[1] == kleuren[2]:
        antwoord = True

    return antwoord

def verf_verzamelen(kleuren):
    rood = kleuren.count('rood')
    groen = kleuren.count('groen')
    blauw = kleuren.count('blauw')

    min_rg = min(rood, groen)
    min_alles = min(min_rg, blauw)

    element_2 = [min_alles, min_alles, min_alles]
    element_1 = sum(element_2)

    return element_1, element_2


# begin = [0,0,0]
#begin = kleur_toevoegen(begin, kleuren[0])

print(verf_verzamelen(['blauw', 'rood', 'groen', 'blauw', 'groen', 'rood', 'blauw', 'rood', 'blauw', 'rood', 'rood', 'blauw', 'blauw', 'rood', 'groen', 'rood', 'groen']))



