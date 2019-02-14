def ontdubbelen(woord):
    for i in range(0, len(woord)):
        while woord[i] == woord[i+1]:
            woord = woord[:i] + woord[i+1:]

    return woord

print(ontdubbelen('stressstoornissen'))
