aanvaller1 = int(input('het aantal ogen van aanvaller 1: '))
aanvaller2 = int(input('het aantal ogen van aanvaller 2: '))
aanvaller3 = int(input('het aantal ogen van aanvaller 3: '))
verdediger1 = int(input('het aantal ogen van verdediger 1: '))
verdediger2 = int(input('het aantal ogen van verdediger 2: '))

#invoer
a = max(aanvaller1, aanvaller2, aanvaller3)
b = max(verdediger1, verdediger2)
c = aanvaller1 + aanvaller2 + aanvaller3 - a - min(aanvaller1, aanvaller2, aanvaller3)
d = min(verdediger1, verdediger2)

if a > b:
    if c > d:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif c < d or c == d:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a < b:
    if c > d:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
    elif c < d or c == d:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
elif a == b:
    if c == d:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    elif c > d:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
    elif c < d:
        print('aanvaller verliest 2 leger, verdediger verliest O legers')