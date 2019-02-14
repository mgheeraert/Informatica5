zin = str(input('zin: '))
tweet = ''

for i in range(0, len(zin)):
    if zin[i] == '#':
        woord = zin[i:].find(' ')
        if (woord + i) > i:
            tweet = zin[i + 1:i + woord]
            print(tweet)

