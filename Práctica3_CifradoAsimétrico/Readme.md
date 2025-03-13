# Práctica 2: Criptografía con RSA y ECC

## Descripción
Esta práctica tiene como objetivo implementar operaciones criptográficas utilizando los algoritmos RSA y ECC mediante la librería `pycryptodome` en Python. Se desarrollan funciones para generar claves, cifrar y descifrar mensajes, firmar digitalmente y verificar firmas.

## Archivos y funcionalidades

### 1. `rsa_object.py`
Este archivo define la clase `RSA_OBJECT`, que encapsula la funcionalidad de RSA. Permite:
- **Generar claves RSA (2048 bits)**.
- **Guardar y cargar claves privadas y públicas** en archivos.
- **Cifrar y descifrar mensajes** utilizando PKCS1_OAEP.
- **Firmar y verificar firmas digitales** mediante PKCS PSS.

### 2. `ca.py`
Este script genera y almacena claves RSA para distintos usuarios.

### 3. `alice.py`
Este script:
- Carga la clave privada de Alice y la clave pública de Bob.
- Cifra un mensaje con la clave pública de Bob.
- Firma el mensaje con la clave privada de Alice.
- Guarda el mensaje cifrado y la firma en archivos.

### 4. `bob.py`
Este script:
- Carga la clave privada de Bob y la clave pública de Alice.
- Recupera el mensaje cifrado y la firma.
- Descifra el mensaje y verifica su autenticidad.

## Cómo ejecutar
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
