#invoer
r = int(input('geef r:'))
som_veelvouden = 0

#berekening
for i in range(r, 101, r):
    som_veelvouden += i

#uitvoer
print(som_veelvouden)
