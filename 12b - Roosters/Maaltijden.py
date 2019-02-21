#Middagmaal: € 5.3
#Soep: € 1.7
#Vieruurtje: € 2.3

def maaltijdprijs(maaltijdtype, aantal):

    maaltijdprijs = 0

    if maaltijdtype == 'middagmaal':
        maaltijdprijs = aantal * 5.3
    elif maaltijdtype == 'soep':
        maaltijdprijs = aantal * 1.7
    elif maaltijdtype == 'vieruurtje':
        maaltijdprijs = aantal * 2.3

    return maaltijdprijs

def dagprijs(bestelling):

    dagprijs = 0

    #overloop de bestelling in stapjes van 2
    for i in range(0, len(bestelling), 2):

        dagprijs += maaltijdprijs(bestelling[i], bestelling[i + 1])

    return dagprijs

def weekprijs(bestelling):
    weekprijs = 0

    for dag in bestelling:

        weekprijs += dagprijs(dag)

    return weekprijs