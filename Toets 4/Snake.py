def beweeg(coordinaat, teken):

    nieuwe_coordinaat = list((coordinaat))
    eerste_coordinaat = coordinaat[0]
    tweede_coordinaat = coordinaat[1]

    for i in range(0, len(coordinaat)):
        if teken == '<':
            nieuwe_coordinaat.pop(0)
            nieuwe_coordinaat.insert(0,eerste_coordinaat - 1)
        elif teken == '>':
            nieuwe_coordinaat.pop(0)
            nieuwe_coordinaat.insert(0,eerste_coordinaat + 1)

        elif teken == 'v':
            nieuwe_coordinaat.pop(1)
            nieuwe_coordinaat.insert(1,eerste_coordinaat - 1)

        else:
            nieuwe_coordinaat.pop(1)
            nieuwe_coordinaat.insert(1,eerste_coordinaat + 1)

    return tuple(nieuwe_coordinaat)

def teruggekeerd(lijst):
    antwoord = ''
    if lijst[0] == '>' and lijst[1] == '<':
        antwoord = True
    elif lijst[0] == '<' and lijst[1] == '>':
        antwoord = True
    elif lijst[0] == '^' and lijst[1] == 'v':
        antwoord = True
    elif lijst[0] == 'v' and lijst[1] == '^':
        antwoord = True
    else:
        antwoord = False

    return antwoord

def laatste_levende_positie(lijst):
    begin_punt = [0,0]
    begin = beweeg(begin_punt,lijst[0])
    i = 1
    aantal_zetten = 0

    while teruggekeerd(begin) is False and i in range(len(lijst)):
        begin = beweeg(begin,kleur[i])
            aantal_zetten += 1
            lijst.remove(lijst[0])


    return aantal_zetten, tuple(begin_punt)

print(laatste_levende_positie(['>', '<', '^']))


