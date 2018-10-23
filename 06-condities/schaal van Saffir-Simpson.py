windsnelheid = float(input('Wat is de windsnelheid: '))

#invoer
if 119 <= windsnelheid <= 153:
    print('categorie 1')
elif 154 <= windsnelheid <= 177:
    print ('categorie 2')
elif 178 <= windsnelheid <= 209:
    print('categorie 3')
elif 210 <= windsnelheid <= 249:
    print ('categorie 4')
elif windsnelheid <= 118:
    print('geen orkaan')
else:
    print('categorie 5')
