
def afficher_binaire(E):
    l = []
    for i in range(len(E)):
        if i % 4 == 0:
            if i != 0:
                l.append(" ")
        
        affichage = E[i]
        affichage = str(affichage)

        l.append(affichage)
    l = "".join(l)

    return l

L = [0,0,1,1,1,0,1,0,1]
print(afficher_binaire(L))