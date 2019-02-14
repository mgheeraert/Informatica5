def nieuw_kaartspel(teken, getallen):
    nieuwe_uitkomst = []
    tekens_apart = 0
    getallen_apart = 0
    while tekens_apart in range(0, len(teken)):
        while getallen_apart in range(0, len(getallen)):
            nieuwe_uitkomst.append(teken[tekens_apart] + getallen[getallen_apart])
            getallen_apart += 1
        tekens_apart += 1
        getallen_apart = 0

    return nieuwe_uitkomst

def splits_kaartspel(lijst):
        midden = len(lijst) // 2
        lijst1 = []
        lijst2 = []
        if len(lijst) % 2 == 0:
            lijst1 = len(lijst).split[midden:]
            lijst2 = len(lijst).split[:midden]
        else:
            lijst1 = len(lijst).split[midden - 1:]
            lijst2 = len(lijst).split[:midden]

    return lijst1, lijst2

print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))

