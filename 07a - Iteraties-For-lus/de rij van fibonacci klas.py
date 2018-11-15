#invoer
n = int(input('Hoeveelste getal van fibonacci: '))

vorige = 1
huidige = 1
################################
vorige, huidige = 1, 1

for i in range(n - 2):
    hulp = vorige
    vorige = huidige
    huidige = huidige + hulp
##############################################
    vorige, huidige = huidige, huidige + vorige

print(huidige)