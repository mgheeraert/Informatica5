antwoord_1 = input('antwoord_1: ')
antwoord_2 = input('antwoord_2: ')

#invoer
if antwoord_1 == 'blad'and antwoord_2 =='blad' or antwoord_1 =='schaar' and antwoord_2 == 'schaar' or antwoord_1 == 'steen' and antwoord_2 == 'steen':
    print('onbeslist')
elif antwoord_1 == 'steen':
    if antwoord_2 == 'blad':
        print('speler 2 wint')
    else:
        print('speler 1 wint')
elif antwoord_1 == 'blad':
    if antwoord_2 == 'schaar':
        print('speler 2 wint')
    else:
        print ('speler 1 wint')
elif antwoord_1 == 'schaar':
    if antwoord_2 == 'steen':
        print ('speler 2 wint')
    else:
        print('speler 1 wint')
