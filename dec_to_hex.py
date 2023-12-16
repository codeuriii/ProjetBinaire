def decimal_vers_hex(nombre_decimal, maj=True):
    # Utiliser la fonction hex() pour convertir le décimal en hexadécimal
    hexadecimal = hex(nombre_decimal)
    # La fonction hex() retourne une chaîne au format '0x...', on récupère donc tout après le '0x'
    hexadecimal = hexadecimal[2:]
    
    if maj:
        # Convertir les lettres en majuscules
        hexadecimal = hexadecimal.upper()
    return hexadecimal
