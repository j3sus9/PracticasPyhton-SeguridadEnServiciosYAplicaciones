from Codigo_RSA_CampusVirtual import crear_RSAKey, guardar_RSAKey_Privada, guardar_RSAKey_Publica

def generar_claves():
    # Crear claves para Alice
    key_alice = crear_RSAKey()
    guardar_RSAKey_Privada("alice_private.pem", key_alice, "alice_password")
    guardar_RSAKey_Publica("alice_public.pem", key_alice)

    # Crear claves para Bob
    key_bob = crear_RSAKey()
    guardar_RSAKey_Privada("bob_private.pem", key_bob, "bob_password")
    guardar_RSAKey_Publica("bob_public.pem", key_bob)

generar_claves()