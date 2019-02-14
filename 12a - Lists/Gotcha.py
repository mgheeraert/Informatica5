def ik_heb_gemoord(namen, uitvoerder):

    i = namen.index(uitvoerder)

    if i < len(namen) - 2:
        woord = namen[i + 2]
        namen.pop(i + 1)
    elif i == len(namen) - 2:
        woord = namen[0]
        namen.pop(len(namen)-1)
    elif len(namen) == 1:
        woord = namen[0]
        namen = [uitvoerder]
    else:
        woord = namen[1]
        namen.pop(0)

    return woord, namen
print(ik_heb_gemoord(['jan'],'jan'))

def ik_ben_vermoord(namen, slachtoffer):

    i = namen.index(slachtoffer)
    if len(namen) == 1:
        woord = namen[i]
    elif i == len(namen) - 1:
        woord = namen[0]
        namen.pop(i)
    else:
        woord = namen[i + 1]
        namen.pop(i)

    return woord, namen
