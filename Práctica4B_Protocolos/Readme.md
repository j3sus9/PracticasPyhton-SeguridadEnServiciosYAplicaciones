# Práctica 4B: Protocolo Asimétrico Autenticado — README

Este repositorio contiene la implementación completa de la **Práctica 4B** de la asignatura de Seguridad en Servicios y Aplicaciones. En ella se aborda un protocolo de distribución de claves con un TTP (Third-Trusted Party), y un intercambio seguro entre Alice y Bob mediante AES-GCM y AES-CTR con HMAC.

---

## Estructura de ficheros

- `funciones_aes.py`: librería de utilidad con funciones para:
  - Generar claves AES-128 (`crear_AESKey`).
  - Cifrar/descifrar en modo **GCM** (un único mensaje).  
  - Cifrar/descifrar en modo **CTR** (varios mensajes) con HMAC externo.

- `p-t.py`: implementa al **TTP (Trusted Third Party)**.
  1. Genera y persiste `KAT.bin` y `KBT.bin`.
  2. Atiende conexiones de **Bob** (puerto 5551): recibe `("Bob", Nb)` cifrado en AES‑GCM, responde con `(K1, K2, Nb)` en AES‑GCM.
  3. Atiende conexiones de **Alice** (puerto 5552): recibe `("Alice", Na)` cifrado en AES‑GCM, responde con `(K1, K2, Na)` en AES‑GCM.

- `p-b.py`: implementa a **Bob**.
  1. Lee `KBT.bin`.
  2. Conecta con TTP en 5551, envía `("Bob", Nb)` y recibe `(K1, K2, Nb)` en AES‑GCM.
  3. Escucha en 5553 y realiza el intercambio con Alice:
     - Paso 5 (recibir Nombre): AES‑CTR + HMAC.
     - Paso 6 (enviar Apellido): AES‑CTR + HMAC.
     - Paso 7 (recibir "END"): AES‑CTR + HMAC.

- `p-a.py`: implementa a **Alice**.
  1. Lee `KAT.bin`.
  2. Conecta con TTP en 5552 (misma conexión): envía `("Alice", Na)` y recibe `(K1, K2, Na)` en AES‑GCM.
  3. Conecta con Bob en 5553 y realiza el intercambio:
     - Paso 5 (enviar Nombre): AES‑CTR + HMAC.
     - Paso 6 (recibir Apellido): AES‑CTR + HMAC.
     - Paso 7 (enviar "END"): AES‑CTR + HMAC.

- `socket_class.py`: clase simplificada para envío/recepción TCP con prefijo de longitud.

---

## Requisitos

- Python 3.8+  
- PyCryptodome  
```bash
pip install pycryptodome
```

---

## Ejecución

1. **Inicia el TTP**:
   ```bash
   python p-t.py
   ```

2. **Ejecuta a Bob** (cuando T muestre "Esperando a Bob…"):
   ```bash
   python p-b.py
   ```

3. **Ejecuta a Alice** (cuando Bob muestre "esperando mensaje de Alice…"):
   ```bash
   python p-a.py
   ```

Si todo funciona, verás en consola la secuencia de mensajes cifrados y los prints finales indicando que el protocolo concluyó con éxito.

---

## Notas

- **AES‑GCM** sólo para un mensaje (intercambio con TTP).  
- **AES‑CTR + HMAC** para comunicación bidireccional (varios mensajes).
- Asegúrate de respetar el orden de arranque (TTP → Bob → Alice) y de no reiniciar sockets antes de haberlos cerrado.

---

¡Práctica completada con éxito! Espero tus comentarios o dudas.
