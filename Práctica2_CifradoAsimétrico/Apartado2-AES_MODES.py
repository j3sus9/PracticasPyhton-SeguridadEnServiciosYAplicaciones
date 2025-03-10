from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter

DATA = "Hola Amigos de Seguridad".encode("utf-8")
KEY = get_random_bytes(16)   # Clave aleatoria de 128 bits
BLOCK_SIZE_AES = 16          # Bloque de 128 bits

# a)
def ecb(data):
    print("\nECB:")
    print(data.decode("utf-8", "ignore"))
    cipher = AES.new(KEY, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_AES))
    print(ciphertext)

    decipher = AES.new(KEY, AES.MODE_ECB)
    new_data = unpad(decipher.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
    print(new_data)

# b)
def ctr(data):
    print("\nCTR:")
    print(data.decode("utf-8", "ignore"))
    nonce = get_random_bytes(int(BLOCK_SIZE_AES / 2))
    cipher = AES.new(KEY, AES.MODE_CTR, nonce = nonce)
    ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_AES))
    print(ciphertext)

    decipher = AES.new(KEY, AES.MODE_CTR, nonce = nonce)
    new_data = unpad(decipher.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
    print(new_data)

# c)
def ofb(data):
    print("\nOFB:")
    print(data.decode("utf-8", "ignore"))
    IV = get_random_bytes(16)    # IV aleatorio de 64 bitspara CBC
    cipher = AES.new(KEY, AES.MODE_OFB, IV)
    ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_AES))
    print(ciphertext)

    decipher = AES.new(KEY, AES.MODE_OFB, IV)
    new_data = unpad(decipher.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
    print(new_data)

# d)
def cfb(data):
    print("\nCFB:")
    print(data.decode("utf-8", "ignore"))
    IV = get_random_bytes(16)    # IV aleatorio de 64 bitspara CBC
    cipher = AES.new(KEY, AES.MODE_CFB, IV)
    ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_AES))
    print(ciphertext)

    decipher = AES.new(KEY, AES.MODE_CFB, IV)
    new_data = unpad(decipher.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
    print(new_data)

# e)
def gcm(data):
    print("\nGCM:")
    print(data.decode("utf-8", "ignore"))
    nonce = get_random_bytes(int(BLOCK_SIZE_AES / 2))
    cipher = AES.new(KEY, AES.MODE_GCM, nonce = nonce, mac_len=16)
    ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE_AES))
    print(ciphertext)

    decipher = AES.new(KEY, AES.MODE_GCM, nonce = nonce, mac_len=16)
    new_data = unpad(decipher.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
    print(new_data)


# Ejecucion de los algoritmos de cifrado/descifrado

ecb(DATA) # a
ctr(DATA) # b
ofb(DATA) # c
cfb(DATA) # d
gcm(DATA) # e
