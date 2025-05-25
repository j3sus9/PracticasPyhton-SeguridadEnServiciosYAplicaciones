# Práctica: Análisis de Protocolos de Seguridad

Este repositorio contiene los análisis realizados sobre capturas reales de tráfico de red de protocolos seguros e inseguros, en el marco de la asignatura *Seguridad en Servicios y Aplicaciones*.

## 📋 Contenido de la práctica

### 📡 Ejercicio 1: TELNET y FTP

Análisis de sesiones capturadas para protocolos en texto plano:

- Identificación de IP cliente y servidor
- Extracción de credenciales
- Determinación del sistema remoto
- Comandos ejecutados en cada sesión

### 🔐 Ejercicio 2: SSH

Estudio detallado de una sesión SSH:

- Identificación de negociación de claves
- Momento exacto en que comienza el cifrado
- Algoritmos criptográficos aplicados
- Autenticación utilizada y posibles errores

### 📜 Ejercicio 3: TLS

Análisis del protocolo TLS a bajo nivel:

- Handshake vs. tráfico de aplicación
- Versiones utilizadas de TLS y negociación
- Suites de cifrado soportadas y seleccionada
- Certificados digitales: clave pública y key exchange
- Verificación de autenticación mutua
- Análisis de nonces y encapsulamientos de mensajes

## 🧰 Herramientas utilizadas

- Wireshark (análisis de capturas `.pcap` o `.pcapng`)
- Visualización de tramas TLS, SSH, FTP y TELNET

## ✅ Requisitos para evaluación

- Respuestas razonadas y justificadas
- Capturas o evidencias visuales de Wireshark
- Conclusiones claras sobre seguridad de cada protocolo