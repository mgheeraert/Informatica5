def geldige_zet(zet):
    if zet[0] in 'KDTPL':
        if zet[1] in 'abcdefgh' and zet[2] in '12345678':
            message = True

    else:
        if zet[0] in 'abcdefgh' and zet[1] in '12345678':
            message = True
        else:
            message = False


    return message

def geldige_zetten(zetten):
    i = 0
    message = True

    while message == 'True' and i in range(0, len(zetten)-1):
        nieuwe_zet = zetten[i]
        message = geldige_zet(nieuwe_zet)
        i += 1


    return message



