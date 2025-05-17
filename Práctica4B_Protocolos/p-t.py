from Crypto.Hash import SHA256, HMAC
import base64
import json
import sys
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes

# Paso 0: Crea las claves que T comparte con B y A
##################################################

# Crear Clave KAT, guardar a fichero
KAT = funciones_aes.crear_AESKey()
FAT = open("KAT.bin", "wb")
FAT.write(KAT)
FAT.close()

# Crear Clave KBT, guardar a fichero
KBT = funciones_aes.crear_AESKey()
FBT = open("KBT.bin", "wb")
FBT.write(KBT)
FBT.close()

# Paso 1) B->T: KBT(Bob, Nb) en AES-GCM
#######################################

# Crear el socket de escucha de Bob (5551)
print("Esperando a Bob...")
socket_Bob = SOCKET_SIMPLE_TCP('127.0.0.1', 5551)
socket_Bob.escuchar()

# Crea la respuesta para B y A: K1 y K2
K1 = funciones_aes.crear_AESKey()
K2 = funciones_aes.crear_AESKey()

# Recibe el mensaje
cifrado = socket_Bob.recibir()
cifrado_mac = socket_Bob.recibir()
cifrado_nonce = socket_Bob.recibir()

# Descifro los datos con AES GCM
datos_descifrado_ET = funciones_aes.descifrarAES_GCM(KBT, cifrado_nonce, cifrado, cifrado_mac)

# Decodifica el contenido: Bob, Nb
json_ET = datos_descifrado_ET.decode("utf-8" ,"ignore")
print("B->T (descifrado): " + json_ET)
msg_ET = json.loads(json_ET)

# Extraigo el contenido
t_bob, t_nb = msg_ET
t_nb = bytearray.fromhex(t_nb)

# Paso 2) T->B: KBT(K1, K2, Nb) en AES-GCM
##########################################

msg_TB = [K1.hex(), K2.hex(), t_nb.hex()]
json_TB = json.dumps(msg_TB).encode("utf-8")
aes_TB = funciones_aes.iniciarAES_GCM(KBT)
cifrado_TB, mac_TB, nonce_TB = funciones_aes.cifrarAES_GCM(aes_TB, json_TB)
socket_Bob.enviar(cifrado_TB)
socket_Bob.enviar(mac_TB)
socket_Bob.enviar(nonce_TB)

# Cerramos el socket entre B y T, no lo utilizaremos mas
socket_Bob.cerrar() 

# Paso 3) A->T: KAT(Alice, Na) en AES-GCM
#########################################

print("Esperando a Alice...")
socket_Alice = SOCKET_SIMPLE_TCP('127.0.0.1', 5552)
socket_Alice.escuchar()

# Recibe el mensaje
cifrado = socket_Alice.recibir()
cifrado_mac = socket_Alice.recibir()
cifrado_nonce = socket_Alice.recibir()

# Descifro los datos con AES GCM
datos_descifrado_AT = funciones_aes.descifrarAES_GCM(KAT, cifrado_nonce, cifrado, cifrado_mac)

# Decodifica el contenido: Alice, Na
json_AT = datos_descifrado_AT.decode("utf-8" ,"ignore")
print("A->T (descifrado): " + json_AT)
msg_AT = json.loads(json_AT)

# Extraigo el contenido
t_alice, t_na = msg_AT

# Paso 4) T->A: KAT(K1, K2, Na) en AES-GCM
##########################################

msg_TA = [K1.hex(), K2.hex(), t_na]
json_TA = json.dumps(msg_TA).encode("utf-8")
aes_TA = funciones_aes.iniciarAES_GCM(KAT)
cifrado_TA, mac_TA, nonce_TA = funciones_aes.cifrarAES_GCM(aes_TA, json_TA)
socket_Alice.enviar(cifrado_TA)
socket_Alice.enviar(mac_TA)
socket_Alice.enviar(nonce_TA)

# Cerramos el socket entre A y T
socket_Alice.cerrar()

print("[T] Protocolo completado.")
