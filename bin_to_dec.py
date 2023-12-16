
def binaire_vers_decimal(liste_binaire):
    # Vérifier si la liste est vide
    if not liste_binaire:
        return None
    
    # Utiliser la fonction join pour concaténer les chiffres binaires en une chaîne
    chaine_binaire = ''.join(map(str, liste_binaire))
    
    # Utiliser la fonction int() pour convertir la chaîne binaire en décimal
    nombre_decimal = int(chaine_binaire, 2)
    
    return nombre_decimal
