from Crypto.Hash import SHA256, HMAC
import json
from socket_class import SOCKET_SIMPLE_TCP
import funciones_aes
from Crypto.Random import get_random_bytes

# Paso 0: Inicialización
KAT = open("KAT.bin", "rb").read()

# Conectamos una sola vez al TTP (puerto 5552) para Paso 3 y Paso 4
sock_t = SOCKET_SIMPLE_TCP('127.0.0.1', 5552)
sock_t.conectar()

# Paso 3) A->T: KAT(Alice, Na) en AES-GCM
na = get_random_bytes(16)
msg = ["Alice", na.hex()]
json_msg = json.dumps(msg).encode("utf-8")
aes_gcm = funciones_aes.iniciarAES_GCM(KAT)
c1, mac1, n1 = funciones_aes.cifrarAES_GCM(aes_gcm, json_msg)
sock_t.enviar(c1)
sock_t.enviar(mac1)
sock_t.enviar(n1)

# Paso 4) T->A: KAT(K1, K2, Na) — mis­ma conexión
d1 = sock_t.recibir()
m1 = sock_t.recibir()
n2 = sock_t.recibir()
plain = funciones_aes.descifrarAES_GCM(KAT, n2, d1, m1)
k1_hex, k2_hex, na_r = json.loads(plain.decode("utf-8"))
assert na_r == na.hex()
K1 = bytes.fromhex(k1_hex)
K2 = bytes.fromhex(k2_hex)
sock_t.cerrar()

# Paso 5) A->B: KAB(Nombre) en AES-CTR con HMAC (puerto 5553)
sock_ab = SOCKET_SIMPLE_TCP('127.0.0.1', 5553)
sock_ab.conectar()
aes_ctr_enc, nonce5 = funciones_aes.iniciarAES_CTR_cifrado(K1)
ct5 = funciones_aes.cifrarAES_CTR(aes_ctr_enc, b"Alice")
hm5 = HMAC.new(K2, ct5, digestmod=SHA256).digest()
sock_ab.enviar(nonce5)
sock_ab.enviar(ct5)
sock_ab.enviar(hm5)

# Paso 6) B->A: KAB(Apellido) en AES-CTR con HMAC
nonce6 = sock_ab.recibir()
ct6 = sock_ab.recibir()
hm6 = sock_ab.recibir()
aes_ctr_dec = funciones_aes.iniciarAES_CTR_descifrado(K1, nonce6)
pt6 = funciones_aes.descifrarAES_CTR(aes_ctr_dec, ct6)
HMAC.new(K2, ct6, digestmod=SHA256).verify(hm6)
print("Apellido recibido de B:", pt6.decode())

# Paso 7) A->B: KAB(END) en AES-CTR con HMAC
aes_ctr_enc2, nonce7 = funciones_aes.iniciarAES_CTR_cifrado(K1)
ct7 = funciones_aes.cifrarAES_CTR(aes_ctr_enc2, b"END")
hm7 = HMAC.new(K2, ct7, digestmod=SHA256).digest()
sock_ab.enviar(nonce7)
sock_ab.enviar(ct7)
sock_ab.enviar(hm7)
sock_ab.cerrar()
