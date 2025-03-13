# Práctica 2: Criptografía con RSA y ECC

## Descripción
Esta práctica tiene como objetivo implementar operaciones criptográficas utilizando los algoritmos RSA y ECC mediante la librería `pycryptodome` en Python. Se desarrollan funciones para generar claves, cifrar y descifrar mensajes, firmar digitalmente y verificar firmas.

## Apartados

### 1. Implementación de RSA (`rsa_object.py`)
Este apartado se basa en la implementación de RSA y sus operaciones básicas:
- **Generar claves RSA (2048 bits)**.
- **Guardar y cargar claves privadas y públicas** en archivos.
- **Cifrar y descifrar mensajes** utilizando PKCS1_OAEP.
- **Firmar y verificar firmas digitales** mediante PKCS PSS.

### 2. Implementación de ECC (`ecc.py`)
En este apartado se implementan las funciones básicas para trabajar con criptografía de curvas elípticas (ECC):
- **Generar claves ECC (NIST P-256)**.
- **Guardar y cargar claves privadas y públicas**.
- **Firmar y verificar firmas digitales** con el esquema DSS y SHA-256.
- **Nota**: `pycryptodome` aún no soporta cifrado con ECC, por lo que solo se implementa la firma y verificación.

### 3. Implementación basada en RSA (`rsa_object.py`)
Se crea una clase `RSA_OBJECT` que encapsula todas las operaciones de RSA, permitiendo:
- Crear claves RSA y almacenarlas.
- Cifrar y descifrar datos.
- Firmar y verificar mensajes.
- Ejecutar correctamente el código de prueba indicado en la práctica.

## Cómo ejecutar (Ejemplo con apartado 1)
1. **Generar las claves RSA**
   ```bash
   python ca.py
   ```
2. **Procesar y firmar un mensaje con Alice**
   ```bash
   python alice.py
   ```
3. **Descifrar y verificar la firma con Bob**
   ```bash
   python bob.py
   ```

## Notas adicionales
- Se recomienda instalar `pycryptodome` si aún no está presente:
  ```bash
  pip install pycryptodome
  ```
- El cifrado con ECC aún no está implementado en `pycryptodome`, por lo que solo se usa para firma y verificación.
