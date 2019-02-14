def hint(geraden_woord, woord):
    antwoord = ''
    for i in range(0, len(geraden_woord)):
        if geraden_woord[i] in woord:
            if geraden_woord[i] == woord[i]:
                antwoord += geraden_woord[i].upper()
            else:
                antwoord += geraden_woord[i]
        else:
            antwoord += '.'

    return antwoord


