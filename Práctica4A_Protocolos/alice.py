import os, json
from socket_class import SOCKET_SIMPLE_TCP
from Crypto.Hash import HMAC, SHA256
import funciones_aes, funciones_rsa

# 1. Conectar con Bob
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()

# 2. Enviar nombre y nonce
nonce = os.urandom(16)
mensaje = ["Alice", nonce.hex()]
socket.enviar(json.dumps(mensaje).encode())

# 3. Recibir respuesta de Bob
respuesta = json.loads(socket.recibir().decode())
nombre_bob, nonce_hex = respuesta
if nombre_bob != "Bob" or nonce_hex != nonce.hex():
    print("Error: Bob no es quien dice ser")
    socket.cerrar()
    exit()

# 4. Generar claves K1 y K2
K1 = funciones_aes.crear_AESKey()
K2 = funciones_aes.crear_AESKey()
K1_K2 = K1 + K2

# 5. Cargar claves y preparar datos
clave_publica_bob = funciones_rsa.cargar_RSAKey_Publica("rsa_bob.pub")
K1_cif = funciones_rsa.cifrarRSA_OAEP_BIN(K1, clave_publica_bob)
K2_cif = funciones_rsa.cifrarRSA_OAEP_BIN(K2, clave_publica_bob)

clave_privada_alice = funciones_rsa.cargar_RSAKey_Privada("rsa_alice.pem", "alice")
firma = funciones_rsa.firmarRSA_PSS(K1_K2, clave_privada_alice)

# 6. Enviar claves cifradas y firma
mensaje = [K1_cif.hex(), K2_cif.hex(), firma.hex()]
socket.enviar(json.dumps(mensaje).encode())

# 7. Recibir mensaje cifrado + HMAC de Bob
mensaje_bob = json.loads(socket.recibir().decode())
cifrado = bytes.fromhex(mensaje_bob[0])
hmac_recibido = bytes.fromhex(mensaje_bob[1])
nonce_k1 = bytes.fromhex(mensaje_bob[2])

aes_descifrado = funciones_aes.iniciarAES_CTR_descifrado(K1, nonce_k1)
mensaje = funciones_aes.descifrarAES_CTR(aes_descifrado, cifrado)

# Verificar integridad
h = HMAC.new(K2, mensaje, digestmod=SHA256)
try:
    h.verify(hmac_recibido)
    print("Mensaje de Bob:", mensaje.decode())
except:
    print("HMAC no válido de Bob")
    socket.cerrar()
    exit()

# 8. Enviar mensaje cifrado + HMAC a Bob
mensaje_claro = b"Hola Amigos"
aes_cifrado, nonce_k1 = funciones_aes.iniciarAES_CTR_cifrado(K1)
cifrado = funciones_aes.cifrarAES_CTR(aes_cifrado, mensaje_claro)
hmac = HMAC.new(K2, mensaje_claro, digestmod=SHA256).digest()

mensaje = [cifrado.hex(), hmac.hex(), nonce_k1.hex()]
socket.enviar(json.dumps(mensaje).encode())

socket.cerrar()
