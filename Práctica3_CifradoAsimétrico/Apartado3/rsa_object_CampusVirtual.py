from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256

class RSA_OBJECT:
    def __init__(self):
        """Inicializa un objeto RSA, sin ninguna clave"""
        self.private_key = None
        self.public_key = None

    def create_KeyPair(self):
        """Crea un par de claves publico/privada, y las almacena dentro de la instancia"""
        key = RSA.generate(2048)
        self.private_key = key
        self.public_key = key.publickey()

    def save_PrivateKey(self, file, password):
        """Guarda la clave privada self.private_key en un fichero file, usando una contraseña password"""
        if self.private_key:
            key_cifrada = self.private_key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
            with open(file, "wb") as f:
                f.write(key_cifrada)

    def load_PrivateKey(self, file, password):
        """Carga la clave privada self.private_key de un fichero file, usando una contraseña password"""
        with open(file, "rb") as f:
            key_cifrada = f.read()
            self.private_key = RSA.import_key(key_cifrada, passphrase=password)
            self.public_key = self.private_key.publickey()

    def save_PublicKey(self, file):
        """Guarda la clave publica self.public_key en un fichero file"""
        if self.public_key:
            key_pub = self.public_key.export_key()
            with open(file, "wb") as f:
                f.write(key_pub)

    def load_PublicKey(self, file):
        """Carga la clave publica self.public_key de un fichero file"""
        with open(file, "rb") as f:
            keyFile = f.read()
            self.public_key = RSA.import_key(keyFile)

    def cifrar(self, datos):
        """Cifra el parámetro datos (de tipo binario) con la clave self.public_key, y devuelve el resultado"""
        if self.public_key:
            try:
                cipher = PKCS1_OAEP.new(self.public_key)
                return cipher.encrypt(datos)
            except Exception:
                return None

    def descifrar(self, cifrado):
        """Descifra el parámetro cifrado (de tipo binario) con la clave self.private_key"""
        if self.private_key:
            try:
                cipher = PKCS1_OAEP.new(self.private_key)
                return cipher.decrypt(cifrado)
            except Exception:
                return None

    def firmar(self, datos):
        """Firma el parámetro datos (de tipo binario) con la clave self.private_key"""
        if self.private_key:
            try:
                h = SHA256.new(datos)
                return pss.new(self.private_key).sign(h)
            except Exception:
                return None

    def comprobar(self, text, signature):
        """Comprueba el parámetro text con respecto a una firma signature usando la clave self.public_key"""
        if self.public_key:
            try:
                h = SHA256.new(text)
                verifier = pss.new(self.public_key)
                verifier.verify(h, signature)
                return True
            except (ValueError, TypeError):
                return False
        return False


# Crear clave RSA
# y guardar en ficheros la clave privada (protegida) y publica
password = "password"
private_file = "rsa_key.pem"
public_file = "rsa_key.pub"
RSA_key_creator = RSA_OBJECT()
RSA_key_creator.create_KeyPair()
RSA_key_creator.save_PrivateKey(private_file, password)
RSA_key_creator.save_PublicKey(public_file)
# Crea dos clases, una con la clave privada y otra con la clave publica
RSA_private = RSA_OBJECT()
RSA_public = RSA_OBJECT()
RSA_private.load_PrivateKey(private_file, password)
RSA_public.load_PublicKey(public_file)
# Cifrar y Descifrar con PKCS1 OAEP
cadena = "Lo desconocido es lo contrario de lo conocido. Pasalo."
cifrado = RSA_public.cifrar(cadena.encode("utf‐8"))
print(cifrado)
descifrado = RSA_private.descifrar(cifrado).decode("utf‐8")
print(descifrado)
# Firmar y comprobar con PKCS PSS
firma = RSA_private.firmar(cadena.encode("utf‐8"))
if RSA_public.comprobar(cadena.encode("utf‐8"), firma):
    print("La firma es valida")
else:
    print("La firma es invalida")