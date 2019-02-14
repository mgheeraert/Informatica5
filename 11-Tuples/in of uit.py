from math import sqrt

def binnen_of_buiten(m, c, p):
    r = sqrt((m[0]-c[0])**2 + (m[1]-c[1])**2)
    d_mp = sqrt((m[0]-p[0])**2 + (m[1]-p[1])**2)

    print(r, d_mp)

    if r == d_mp:
        message = ('op', r)
    elif r < d_mp:
        message = ('buiten', round(d_mp, 4))
    else:
        message = ('binnen', round(d_mp, 4))

    return message

print(binnen_of_buiten((17, 31),(-10, 6),(-6, 26)))
