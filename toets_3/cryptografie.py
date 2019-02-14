def versleutel_woord(woord, parameter):
    for i in range(0, len(woord)):
        if woord[i] == 'abcdefghijklmnopqrstuvwxyz':
            woord = woord[:i] + woord[i].upper() + woord[i+1:]

            if parameter < 32:
                woord = ord(chr(woord[i]) + parameter)
                if woord[i] == '@':
                    woord = woord[i].replace('@', ' ')

                    if woord[i] == ' ':
                        woord = woord[i].replace(' ', '@')


    return woord
print(versleutel_woord('hlaiehf'))
