def versleutel_woord(woord):
    versleutel_woord = ''

    woord = woord.upper()

    for letter in woord:

        versleutel_letter = chr(ord(letter) + n)
        if versleutel_letter  '@:
            versleutel_letter = ' '

        versleutel_woord += versleutel_letter

    return versleutel_woord

def versleutel_zin(zin, getal):

    index_spatie = zin.find(' ')
