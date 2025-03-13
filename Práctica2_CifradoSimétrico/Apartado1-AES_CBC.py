from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter

# AES en modo CBC

key = bytes(b'\x9b\x07\x8c\x85\x82D\xbf\xd0\x9cnz\xf1~AvM')
IV = bytes(b'\xc5\xd2\xc9\xbe\xe2\x94N\x81x\xf1\xa5\x13\x91\xa5\xd9\xfa')

BLOCK_SIZE_AES = 16          # Bloque de 128 bits
data = "Hola amigos de la seguridad".encode("utf-8")
print(data)

# CIFRADO

# Creamos un mecanismo de cifrado AES en modo CBC con un vector de inicialización IV
cipher = AES.new(key, AES.MODE_CBC, IV)

# Ciframos, haciendo que la variable “data”sea múltiplo del tamaño de bloque
ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_AES))
print(ciphertext)


# DESCIFRADO

# Creamos un mecanismo de (des)cifrado AES en modo CBC con un vector de inicialización IV para CBC
# Ambos, cifrado y descifrado, se crean de la misma forma
decipher_des = AES.new(key, AES.MODE_CBC, IV)

# Desciframos, eliminamos el padding, y recuperamos la cadena
new_data = unpad(decipher_des.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")

# Imprimimos los datos descifrados
print(new_data)

"""
b'Hola amigos de la seguridad'
b'\xeb\xc4\xb3:\xf9\x87b4(\x95\xcd$\xcb+\xb9\rz\xee\xd7\xeeEu\x10KFB=\x14^\x96\xeaQ'
Hola amigos de la seguridad
"""

"""
b'Hola amigas de la seguridad'
b'\xb0\xf7\xe6/\xdeki\xa3~\xb4\x8e\x0eN\xc0\xcd\x9eL\x0c\xbb7\xbb\x90.\xc5>H\x0f\xe2\xae\xf3\x13\xe9'
Hola amigas de la seguridad
"""

#CAMBIO DE O POR A EN EL MENSAJE:
# En AES-CBC, cada bloque de texto plano se XOR con el bloque cifrado anterior antes de ser cifrado. 
# Esto significa que un pequeño cambio en el texto original puede afectar significativamente el resultado cifrado.