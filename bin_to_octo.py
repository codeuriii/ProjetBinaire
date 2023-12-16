
from dec_to_bin import decimal_vers_binaire

puissances = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7"
}

def decimal_vers_octets(nbr):
    liste_binaire = decimal_vers_binaire(nbr)
    l = []
    m = []
    p = []
    o = []
    for i in range(len(liste_binaire)):
        if i % 3 == 0:
            if i != 0:
                l.append(" ")
        
        affichage = liste_binaire[i]
        affichage = str(affichage)

        l.append(affichage)
        
    l = "".join(l)
    j = l.replace(" ", "")

    for i in range(len(j)):
        k = len(j) - i - 1
        # print(k)

        m.append(j[k])

    m = ''.join(m)

    for i in range(len(m)):
        if i % 3 == 0:
            if i != 0:
                p.append(" ")
        
        affichage = m[i]
        affichage = str(affichage)

        p.append(affichage)

    p = "".join(p)

    for i in range(len(p)):
        k = len(p) - i - 1
        # print(k)

        o.append(p[k])

    o = ''.join(o)

    return o


print(decimal_vers_octets(26))