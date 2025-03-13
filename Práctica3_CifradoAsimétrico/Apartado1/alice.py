from Codigo_RSA_CampusVirtual import cargar_RSAKey_Privada, cargar_RSAKey_Publica, cifrarRSA_OAEP, firmarRSA_PSS

def procesar_mensaje():
    # Cargar claves
    key_private_alice = cargar_RSAKey_Privada("alice_private.pem", "alice_password")
    key_public_bob = cargar_RSAKey_Publica("bob_public.pem")

    # Mensaje a cifrar y firmar
    mensaje = "Hola amigos de la seguridad"

    # Cifrar con la clave pública de Bob
    mensaje_cifrado = cifrarRSA_OAEP(mensaje, key_public_bob)

    # Firmar con la clave privada de Alice
    firma = firmarRSA_PSS(mensaje, key_private_alice)

    # Guardar resultados
    open("mensaje_cifrado.bin", "wb").write(mensaje_cifrado)
    open("firma.bin", "wb").write(firma)

procesar_mensaje()
