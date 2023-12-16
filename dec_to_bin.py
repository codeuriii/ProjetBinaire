def decimal_vers_binaire(nombre_decimal):
    # Vérifier si le nombre est nul
    if nombre_decimal == 0:
        return [0]
    
    # Initialiser une liste vide pour stocker les chiffres binaires
    liste_binaire = []
    
    # Convertir le nombre décimal en binaire
    while nombre_decimal > 0:
        # Ajouter le reste de la division par 2 à la liste
        liste_binaire.insert(0, nombre_decimal % 2)
        # Effectuer une division entière par 2
        nombre_decimal //= 2
    
    return liste_binaire
