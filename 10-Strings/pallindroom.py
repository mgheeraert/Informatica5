def is_palindroom(woord):
    antwoord = True
    if len(woord) == 1:
        antwoord = True
    else:
        for i in range(0, len(woord)//2):
            if woord[i] == woord[len(woord) -1 - i] and antwoord != False:
                antwoord = True
            else:
                antwoord = False
    return antwoord

