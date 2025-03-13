from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

def crear_ECCKey():
    # Crear una clave ECC con el estándar NIST P-256
    key = ECC.generate(curve='P-256')
    return key

def guardar_ECCKey_Privada(fichero, key, password):
    # Guardar clave privada en un fichero
    with open(fichero, "wt") as f:
        f.write(key.export_key(format='PEM', passphrase=password, protection="PBKDF2WithHMAC-SHA1AndAES128-CBC"))

def cargar_ECCKey_Privada(fichero, password):
    # Cargar clave privada desde un fichero
    with open(fichero, "rt") as f:
        key = ECC.import_key(f.read(), passphrase=password)
    return key

def guardar_ECCKey_Publica(fichero, key):
    # Guardar clave pública en un fichero
    with open(fichero, "wt") as f:
        f.write(key.public_key().export_key(format='PEM'))

def cargar_ECCKey_Publica(fichero):
    # Cargar clave pública desde un fichero
    with open(fichero, "rt") as f:
        key_pub = ECC.import_key(f.read())
    return key_pub

def firmarECC_PSS(texto, key_private):
    # Firmar el texto con la clave privada ECC usando DSS y SHA-256
    h = SHA256.new(texto.encode("utf-8"))
    signer = DSS.new(key_private, 'fips-186-3')
    signature = signer.sign(h)
    return signature

def comprobarECC_PSS(texto, firma, key_public):
    # Comprobar la firma digital con la clave pública ECC
    h = SHA256.new(texto.encode("utf-8"))
    verifier = DSS.new(key_public, 'fips-186-3')
    try:
        verifier.verify(h, firma)
        return True
    except (ValueError, TypeError):
        return False
