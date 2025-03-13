from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class AES_CIPHER_CBC:
    BLOCK_SIZE_AES = 16  # AES: Bloque de 128 bits

    def __init__(self, key):
        """Inicializa la clave."""
        self.key = key

    def cifrar(self, cadena, IV):
        """Cifra el parámetro cadena (String) con una IV específica y devuelve el texto cifrado binario."""
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        return cipher.encrypt(pad(cadena.encode(), self.BLOCK_SIZE_AES))

    def descifrar(self, cifrado, IV):
        """Descifra el parámetro cifrado (binario) con una IV específica y devuelve la cadena en claro."""
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        return unpad(cipher.decrypt(cifrado), self.BLOCK_SIZE_AES).decode()

# Prueba de la clase
key = get_random_bytes(16)  # Clave aleatoria de 128 bits
IV = get_random_bytes(16)  # IV aleatorio de 128 bits

datos1 = "Hola amigos de la seguridad"
datos2 = "Hola amigas de la seguridad"

d = AES_CIPHER_CBC(key)
cifrado1 = d.cifrar(datos1, IV)
cifrado2 = d.cifrar(datos2, IV)

descifrado1 = d.descifrar(cifrado1, IV)
descifrado2 = d.descifrar(cifrado2, IV)

print("Texto original 1:", datos1)
print("Texto cifrado 1:", cifrado1)
print("Texto descifrado 1:", descifrado1)
print()
print("Texto original 2:", datos2)
print("Texto cifrado 2:", cifrado2)
print("Texto descifrado 2:", descifrado2)