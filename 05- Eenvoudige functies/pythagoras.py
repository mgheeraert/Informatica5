#invoer
a = float(input('geef de lengte van a:'))
b = float(input('geef de lengte van b: '))
c = 'schuine zijde'
from math import sqrt as vierkantswortel

#berekening
rechthoekszijden = vierkantswortel((a**2) + (b**2))
hypotenusa = c

#uitvoer
print( '{} {} {:.2f} {} {} {:.2f} {} {:.2f}'.format('In een rechthoekige driehoek met rechthoekszijden', 'a =', a, 'en', 'b =', b, 'is de schuine zijde', rechthoekszijden))