def is_letter(n):
    if n in'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        x = True
    else:
        x = False
    return x

def roteer_letter(a, b):
    if a in 'abcdefghijklmnopqrstuvwxyz':
        if (ord(a) + b) > ord('z'):
            x = (ord(a) + b) - ord('z')
            geroteerde_letter = chr(ord('a')-1 + x)
        else:
            geroteerde_letter = chr(ord(a) + b)
    else:
        if (ord(a) + b) > ord('Z'):
            x = (ord(a) + b) - ord('Z')
            geroteerde_letter = chr(ord('A') - 1 + x)
        else:
            geroteerde_letter = chr(ord(a) + b)


    return geroteerde_letter

#zeker in toets
def versleutel(a, b):
    boodschap = a
    veranderde_boodschap = ''

    for geroteerde_letter in boodschap:
        if is_letter(geroteerde_letter) == True:
            veranderde_code = roteer_letter(geroteerde_letter, b)
            veranderde_boodschap += veranderde_code
        else:
            veranderde_boodschap += geroteerde_letter

    return veranderde_boodschap


    


