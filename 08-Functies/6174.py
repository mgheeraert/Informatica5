def spits(a):
    cijfer1 = a // 1000
    cijfer2 = (a - (cijfer1 * 1000)) // 100
    cijfer3 = (a - (cijfer1 * 1000) - (cijfer2 * 100)) // 10
    cijfer4 = a - (cijfer1 * 1000) - (cijfer2 * 100) - (cijfer3 * 10)

    return cijfer1, cijfer2, cijfer3, cijfer4

def oplopende_cijfers(a, b, c, d):
    hoogste_getal = max(a, b, c, d)
    laagste_getal = min(a, b, c, d)
    tweede_laagste_getal = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
    tweede_hoogste_getal = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))

    return laagste_getal, tweede_laagste_getal, tweede_hoogste_getal, hoogste_getal

def op_af_getallen(a, b, c, d):
    oplopen = ''
    oplopen += str(a) + str(b) + str(c) + str(d)
    aflopen = ''
    aflopen += str(d) + str(c) + str(b) + str(a)

    return oplopen, aflopen

def verschil ( x, y):
    uitkomst_verschil = str(x) - str(y)

    return uitkomst_verschil

def kaprekar(x):
    ???

