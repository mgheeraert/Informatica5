#invoer
woord = str(input('geef woord: '))
bedrag = int(input('gedraaide bedrag: '))
letter = str(input('welke letter?: '))
som = 0
andere_letters = ''

#berekening
while letter in woord and letter not in andere_letters:
    som += bedrag
    andere_letters += letter
    letter = str(input('welke letter?: '))

if letter not in woord:
    som += 0

#uitvoer
print(som)
