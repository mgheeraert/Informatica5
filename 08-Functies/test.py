def welkom(naam):
    print('Welkom terug ' + naam)

welkom('Lieve Sint')
welkom('Zwarte Piet')

print(welkom('Kerstman'))
#######################################

def discriminant(a, b, c):
 return (b ** 2) - (4 * a * c)

d= discriminant(2,4,2)
print(d)

#######################################
#globale variabelen
appel = 'appel'
banaan = 'banaan'
kers = 'kers'

def print_fruit(appel):
   #lokale variabelen
    appel = 'olifant'
    banaan = 'aapje'
    kers = 'goudvis'
    print(appel, banaan, kers)

print_fruit(banaan)
print(appel, banaan, kers)