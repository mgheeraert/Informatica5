def hoogtemeters(lijstje):

    nieuwe_getal = []

    for i in range(0, len(lijstje)-1):
        if lijstje[i] == lijstje[i + 1]:
            nieuwe_getal += [0]
        elif lijstje[i] > lijstje[i + 1]:
            nieuwe_getal +=[lijstje[i +1] -lijstje[i]]
        else:
            nieuwe_getal += [lijstje[i+1]-lijstje[i]]

    return nieuwe_getal

def dalen_en_stijgen(hoogtemeters):
    dalen = 0
    stijgen = 0
    for i in range(0, len(hoogtemeters)):
         if hoogtemeters[i] < 0:
             dalen +=abs(hoogtemeters[i])
         elif hoogtemeters[i] > 0:
             stijgen += hoogtemeters[i]
         else:
            dalen += 0
            stijgen += 0

    return dalen, stijgen

print(dalen_en_stijgen([-761, 286, -113, 649, -547]))