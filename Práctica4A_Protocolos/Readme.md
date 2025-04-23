# 🛡️ Práctica de Protocolos - Comunicación Segura entre Alice y Bob

Este proyecto implementa una **comunicación segura** entre dos entidades, **Alice** (cliente) y **Bob** (servidor), usando:
- Sockets TCP (`SOCKET_SIMPLE_TCP`)
- Cifrado simétrico con AES en modo CTR
- Integridad con HMAC-SHA256
- Firmas digitales RSA-PSS
- Claves públicas y privadas RSA de 2048 bits

## 🧠 Objetivo

Simular un protocolo de establecimiento seguro de sesión entre dos entidades (Alice y Bob), donde:
- Se verifica la identidad de ambos.
- Se intercambian claves simétricas cifradas con RSA.
- Se asegura la integridad de los mensajes con HMAC.
- Se garantiza la autenticidad con firma digital.


## 🧰 Requisitos

- Python 3.x
- [PyCryptodome](https://pypi.org/project/pycryptodome/)

Instalar dependencias:

```bash
pip install pycryptodome
```

## ⚙️ Ejecución

1. **Generar claves RSA
Ejecuta ca.py para generar claves para Alice y Bob:

```bash
python ca.py
```

2. **Ejecutar Bob (servidor)
En una terminal:

```bash
python bob.py
```

3. **Ejecutar Alice (cliente)
En otra terminal:

```bash
python alice.py
```
