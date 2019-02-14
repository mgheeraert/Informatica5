def palindroom(woord):

    i = 0

    while woord[i] == woord[-i - 1] and i < len(woord) // 2:
        i += 1

    return i == (len(woord) // 2)

print(palindroom('koortsmeetsysteemstrook'))

## snelste manier

 return woord == woord[::-1]