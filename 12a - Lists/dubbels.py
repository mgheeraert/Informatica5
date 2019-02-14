def dubbels(tekst):
    lijst_dub = []

    for item in tekst:

        if tekst.count(item) > 1 and item not in lijst_dub:
            lijst_dub.append(item)

    return lijst_dub