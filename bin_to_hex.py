from bin_to_dec import binaire_vers_decimal
from dec_to_hex import decimal_vers_hex

def binaire_vers_hex(liste_binaire):
    dec = binaire_vers_decimal(liste_binaire)
    hexa = decimal_vers_hex(dec)
    return hexa