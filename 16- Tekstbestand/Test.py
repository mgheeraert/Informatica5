#file = open('klas.txt')

#lijn = file.readline()

#while lijn != '':
#    print(lijn)
#    lijn = file.readline()

#file.close()

#nieuwe manier
#lijnen = []

# with open('klas.txt') as bestand:
#     lijnen = bestand.readlines()
#
# for naam in lijnen:
#     print(naam[::-1])
#
# print('er zitten ' + str(len(lijnen)) + 'personen in de klas')

#nieuwe manier2
nieuwe_leerlingen = ['Alice\n', 'Baptiste']

with open('klas.txt', 'w') as bestand:
    bestand.writelines(nieuwe_leerlingen)