windsnelheid = (input('Wat is de windsnelheid?: '))

#invoer
if windsnelheid >= '119' and windsnelheid <= '249':
    if windsnelheid >= '119' and windsnelheid <= '153':
        print('categorie 1')
    elif windsnelheid >= '154' and windsnelheid <= '177':
        print('caterogie 2')
    elif windsnelheid >= '178' and windsnelheid <= '209':
        print('categorie 3')
    else:
        print('categorie 4')
else:
    if windsnelheid >= '250':
        print('categorie 5')
    else:
        print('geen orkaan')