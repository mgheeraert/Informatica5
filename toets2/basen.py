#invoer
aantal_basen = int(input('aantal basen: '))
base = ''
base_A = 0
base_T = 0
base_C = 0
base_G = 0

#berekening
for _ in range(aantal_basen):
    base += input('geef base: ') + ''
    for letter in 'ATGC':
        if base == 'A':
            base_A += 1
        if base == 'T':
            base_T += 1
        if base == 'C':
            base_C += 1
        if base == 'G':
            base_G += 1



