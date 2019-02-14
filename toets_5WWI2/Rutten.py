def tel_woorden(zin):

    aantal_spaties = 0

    for letter in zin:
        if letter == ' ':
            aantal_spaties += 1

    return aantal_spaties

def tel_woorden_dov(zin):
    lengte = len(zin)
    lengte_z_spaties = len(zin.replace('', ''))
    return lengte - lengte_z_spaties + 1

# return len(zin) - len(zin.replace('', '')) + 1