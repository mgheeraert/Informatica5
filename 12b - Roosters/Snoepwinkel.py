def bereken_prijs(lijst):

    prijs = 0

    #overloop alle boodschappen
    for item in lijst:
        # telkens het element op index 1 optellen bij de totale prijs
        prijs += item[1]

    return prijs

def winkelbriefje(lijst):
    briefje = []
    #overloop alle boodschappen
    for item in lijst:
        #telkens element op index 0 in een aan de nieuwe lijst toevoegen
        briefje += [item[0]]

    return briefje

def sorteer(lijst):
    from operator import itemgetter
    lijst.sort(key=itemgetter (1))
    return lijst
