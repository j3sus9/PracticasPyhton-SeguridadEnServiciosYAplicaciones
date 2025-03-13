from Codigo_RSA_CampusVirtual import cargar_RSAKey_Privada, cargar_RSAKey_Publica, descifrarRSA_OAEP, comprobarRSA_PSS

def verificar_mensaje():
    # Cargar claves
    key_private_bob = cargar_RSAKey_Privada("bob_private.pem", "bob_password")
    key_public_alice = cargar_RSAKey_Publica("alice_public.pem")

    # Cargar mensaje cifrado y firma
    mensaje_cifrado = open("mensaje_cifrado.bin", "rb").read()
    firma = open("firma.bin", "rb").read()

    # Descifrar mensaje
    descifrado = descifrarRSA_OAEP(mensaje_cifrado, key_private_bob)
    print("Mensaje descifrado:", descifrado)

    # Verificar firma
    valido = comprobarRSA_PSS(descifrado, firma, key_public_alice)
    print("Firma válida:", valido)

verificar_mensaje()
