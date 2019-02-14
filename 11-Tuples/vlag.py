def vlag(richting, kleuren):

#indexen
    verticale_strepen = ' | '
    horizontale_strepen = '-'
    message = ''

#horizontaal of verticaal
    for i in range(0, len(kleuren)):
        if richting == 'verticaal':
            message += kleuren[i]
            if i != (len(kleuren) - 1):
                message += verticale_strepen

        elif richting == 'horizontaal':
            message += kleuren[i]
            if i != (len(kleuren)-1):
                message += '\n' + horizontale_strepen + '\n'


    return (message)

print(vlag('horizontaal',('zwart', 'geel', 'rood')))