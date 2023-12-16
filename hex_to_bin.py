from hex_to_dec import hex_vers_decimal
from dec_to_bin import decimal_vers_binaire

def hex_vers_binaire(hexadecimal):
    dec = hex_vers_decimal(hexadecimal)
    binaire = decimal_vers_binaire(dec)
    return binaire