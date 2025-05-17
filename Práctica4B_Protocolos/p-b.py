

from Crypto.Hash import SHA256, HMAC
import base64
import json
import sys
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes
from Crypto.Random import get_random_bytes

# Paso 0: Inicializacion
########################

# Lee clave KBT
KBT = open("KBT.bin", "rb").read()

# Paso 1) B->T: KBT(Bob, Nb) en AES-GCM
#######################################

# Crear el socket de conexion con T (5551)
print("Creando conexion con T...")
print("[B] Sesión establecida, esperando mensaje de Alice en 5553…")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket.conectar()

# Crea los campos del mensaje
t_n_origen = get_random_bytes(16)

# Codifica el contenido (los campos binarios en una cadena) y contruyo el mensaje JSON
msg_TE = []
msg_TE.append("Bob")
msg_TE.append(t_n_origen.hex())
json_ET = json.dumps(msg_TE)
print("B -> T (descifrado): " + json_ET)

# Cifra los datos con AES GCM
aes_engine = funciones_aes.iniciarAES_GCM(KBT)
cifrado, cifrado_mac, cifrado_nonce = funciones_aes.cifrarAES_GCM(aes_engine,json_ET.encode("utf-8"))

# Envia los datos
socket.enviar(cifrado)
socket.enviar(cifrado_mac)
socket.enviar(cifrado_nonce)

# Paso 2) T->B: KBT(K1, K2, Nb) en AES-GCM
##########################################

c = socket.recibir()
mac = socket.recibir()
nonce = socket.recibir()
plain = funciones_aes.descifrarAES_GCM(KBT, nonce, c, mac)
k1, k2, nb2 = json.loads(plain.decode("utf-8"))
k1 = bytes.fromhex(k1)
k2 = bytes.fromhex(k2)
assert nb2 == t_n_origen.hex()

# Cerramos el socket entre B y T, no lo utilizaremos mas
socket.cerrar() 

# Paso 5) A->B: KAB(Nombre) en AES-CTR con HMAC
###############################################

sock_b = SOCKET_SIMPLE_TCP('127.0.0.1', 5553)
sock_b.escuchar()
nonce = sock_b.recibir()
c = sock_b.recibir()
mac = sock_b.recibir()
HMAC.new(k2, c, digestmod=SHA256).verify(mac)
aes_ctr = funciones_aes.iniciarAES_CTR_descifrado(k1, nonce)
data = funciones_aes.descifrarAES_CTR(aes_ctr, c)
print("Nombre recibido de A:", data.decode())

# Paso 6) B->A: KAB(Apellido) en AES-CTR con HMAC
#################################################

aes_ctr, nonce = funciones_aes.iniciarAES_CTR_cifrado(k1)
data = b"Smith"
c = funciones_aes.cifrarAES_CTR(aes_ctr, data)
mac = HMAC.new(k2, c, digestmod=SHA256).digest()
sock_b.enviar(nonce)
sock_b.enviar(c)
sock_b.enviar(mac)

# Paso 7) A->B: KAB(END) en AES-CTR con HMAC
############################################

nonce = sock_b.recibir()
c = sock_b.recibir()
mac = sock_b.recibir()
aes_ctr = funciones_aes.iniciarAES_CTR_descifrado(k1, nonce)
data = funciones_aes.descifrarAES_CTR(aes_ctr, c)
HMAC.new(k2, c, digestmod=SHA256).verify(mac)
if data == b"END":
    print("Fin del protocolo")
sock_b.cerrar()

