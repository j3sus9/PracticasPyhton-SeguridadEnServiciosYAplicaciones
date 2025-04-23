import json
from socket_class import SOCKET_SIMPLE_TCP
from Crypto.Hash import HMAC, SHA256
import funciones_aes, funciones_rsa

# 1. Escuchar conexión
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.escuchar()

# 2. Recibir nombre y nonce
mensaje = json.loads(socket.recibir().decode())
nombre_alice, nonce_hex = mensaje
if nombre_alice != "Alice":
    print("Error: no es Alice")
    socket.cerrar()
    exit()

# 3. Responder con nombre y nonce
respuesta = ["Bob", nonce_hex]
socket.enviar(json.dumps(respuesta).encode())

# 4. Recibir claves cifradas y firma
mensaje = json.loads(socket.recibir().decode())
K1_cif = bytes.fromhex(mensaje[0])
K2_cif = bytes.fromhex(mensaje[1])
firma = bytes.fromhex(mensaje[2])

clave_privada_bob = funciones_rsa.cargar_RSAKey_Privada("rsa_bob.pem", "bob")
K1 = funciones_rsa.descifrarRSA_OAEP_BIN(K1_cif, clave_privada_bob)
K2 = funciones_rsa.descifrarRSA_OAEP_BIN(K2_cif, clave_privada_bob)
K1_K2 = K1 + K2

clave_publica_alice = funciones_rsa.cargar_RSAKey_Publica("rsa_alice.pub")
if not funciones_rsa.comprobarRSA_PSS(K1_K2, firma, clave_publica_alice):
    print("Error: firma inválida")
    socket.cerrar()
    exit()

# 5. Enviar mensaje cifrado + HMAC a Alice
mensaje_claro = b"Hola Amigas"
aes_cifrado, nonce_k1 = funciones_aes.iniciarAES_CTR_cifrado(K1)
cifrado = funciones_aes.cifrarAES_CTR(aes_cifrado, mensaje_claro)
hmac = HMAC.new(K2, mensaje_claro, digestmod=SHA256).digest()

mensaje = [cifrado.hex(), hmac.hex(), nonce_k1.hex()]
socket.enviar(json.dumps(mensaje).encode())

# 6. Recibir mensaje cifrado + HMAC de Alice
mensaje_alice = json.loads(socket.recibir().decode())
cifrado = bytes.fromhex(mensaje_alice[0])
hmac_recibido = bytes.fromhex(mensaje_alice[1])
nonce_k1 = bytes.fromhex(mensaje_alice[2])

aes_descifrado = funciones_aes.iniciarAES_CTR_descifrado(K1, nonce_k1)
mensaje = funciones_aes.descifrarAES_CTR(aes_descifrado, cifrado)

h = HMAC.new(K2, mensaje, digestmod=SHA256)
try:
    h.verify(hmac_recibido)
    print("Mensaje de Alice:", mensaje.decode())
except:
    print("HMAC no válido de Alice")

socket.cerrar()
