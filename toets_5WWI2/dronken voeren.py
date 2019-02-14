
def dronken_voeren(woord):
    nieuw_woord = woord[0]

    for i in range(1, len(woord)):
    #even letter?
        if i % 2 == 0:
            nieuw_woord += woord[i].upper()
    #oneven letter en vorige (even) letter is hoofletterklinker op einde van nieuw woord
        elif woord[i - 1] in 'aeiouAEIOU':
            nieuw_woord += woord[i].upper()
        #elif woord[-1] in 'AEIOU':
        # nieuw_woord += woord[i].upper()

    #oneven letter
        else:
            nieuw_woord += woord[i].lower()



    return nieuw_woord

print(dronken_voeren('dronkenboer'))

