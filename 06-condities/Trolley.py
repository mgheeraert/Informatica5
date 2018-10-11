hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee)')
man_duwen = input('Wordt de man van de grug geduwd? (ja/nee)')

#invoer
if hendel_trekken =='ja':
   if man_duwen == 'ja':
        print('2')
   else:
        print('1')
else:
    if man_duwen == 'ja':
        print('1')
    else:
        print('5')