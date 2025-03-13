from ecc import (
    crear_ECCKey, guardar_ECCKey_Privada, cargar_ECCKey_Privada,
    guardar_ECCKey_Publica, cargar_ECCKey_Publica,
    firmarECC_PSS, comprobarECC_PSS
)

def generar_claves():
    # Crear clave ECC
    key = crear_ECCKey()
    guardar_ECCKey_Privada("ecc_privada.pem", key, "password")
    guardar_ECCKey_Publica("ecc_publica.pem", key)

generar_claves()

def procesar_mensaje():
    # Cargar claves
    key_private = cargar_ECCKey_Privada("ecc_privada.pem", "password")
    key_public = cargar_ECCKey_Publica("ecc_publica.pem")

    # Mensaje a firmar y cifrar
    mensaje = "Hola amigos de la seguridad".encode("utf-8")

    # Firmar con la clave privada
    firma = firmarECC_PSS(mensaje.decode("utf-8"), key_private)

    # Guardar mensaje cifrado y firma
    open("mensaje_cifrado_ecc.bin", "wb").write(mensaje)
    open("firma_ecc.bin", "wb").write(firma)

procesar_mensaje()

def verificar_mensaje():
    # Cargar clave pública
    key_public = cargar_ECCKey_Publica("ecc_publica.pem")

    # Cargar mensaje cifrado y firma
    mensaje = open("mensaje_cifrado_ecc.bin", "rb").read().decode("utf-8")
    firma = open("firma_ecc.bin", "rb").read()

    # Verificar firma
    valido = comprobarECC_PSS(mensaje, firma, key_public)
    print("Firma válida:", valido)

verificar_mensaje()