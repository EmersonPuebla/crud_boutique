"""
VALIDACION MOMENT
"""

import os

def clean():
    os.system("cls")

while True:
    reply = input("Valide la operacion (si - s/no - n):").lower()

    if reply == "s" or "si":
        print("Paso :D")
        os.system("pause")

    elif reply == "n" or "no":
        print("bleh no hay fondos suficientes")
        os.system("pause")

    else:
        print("JAHJAJAJAJ PUTO")
