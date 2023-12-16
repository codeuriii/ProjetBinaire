from bin_to_dec import binaire_vers_decimal
from dec_to_bin import decimal_vers_binaire

def addition_binaire(liste_binaire1, liste_binaire2):
    dec1 = binaire_vers_decimal(liste_binaire1)
    dec2 = binaire_vers_decimal(liste_binaire2)

    result_dec = dec1 + dec2
    result_bin = binaire_vers_decimal(result_dec)

    return result_bin