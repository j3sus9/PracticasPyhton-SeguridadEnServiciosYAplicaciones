def cifradoCesarAlfabetoInglesMAY(cadena, desplazamiento):
    """Devuelve un cifrado Cesar con desplazamiento personalizado (+desplazamiento)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + desplazamiento) % 26) + 65
        if (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + desplazamiento) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

def descifradoCesarAlfabetoInglesMAY(cadena, desplazamiento):
    """Devuelve un cifrado Cesar con desplazamiento personalizado (-desplazamiento)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) - desplazamiento) % 26) + 65
        if (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) - desplazamiento) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

# Pruebas
texto_original = "HeLlO WoRLd"
texto_cifrado = cifradoCesarAlfabetoInglesMAY(texto_original, 10)
texto_descifrado = descifradoCesarAlfabetoInglesMAY(texto_cifrado, 10)

print(f"Texto original: {texto_original}")  # "HELLO WORLD"
print(f"Texto cifrado: {texto_cifrado}")    # "KHOOR ZRUOG"
print(f"Texto descifrado: {texto_descifrado}")  # "HELLO WORLD"