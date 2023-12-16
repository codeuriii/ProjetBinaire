
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

def binaire_vers_decimal(liste_binaire):
    # Vérifier si la liste est vide
    if not liste_binaire:
        return None
    
    # Utiliser la fonction join pour concaténer les chiffres binaires en une chaîne
    chaine_binaire = ''.join(map(str, liste_binaire))
    
    # Utiliser la fonction int() pour convertir la chaîne binaire en décimal
    nombre_decimal = int(chaine_binaire, 2)
    
    return nombre_decimal

# Exemple d'utilisation :
liste_binaire = [1, 0, 1, 0]  # Remplacez cela par votre propre liste
resultat_decimal = binaire_vers_decimal(liste_binaire)
print(f"Le nombre décimal correspondant est : {resultat_decimal}")
