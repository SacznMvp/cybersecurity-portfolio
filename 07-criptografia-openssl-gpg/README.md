# Práctica 7 — Introducción a la Criptografía con OpenSSL y GPG

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados y el informe se agregarán cuando el laboratorio esté hecho.

| Nivel | Requisitos previos |
|---|---|
| 🟡 Intermedio | Prácticas 2 y 3 |

## 📌 Objetivo

Entender hashing, cifrado simétrico, claves públicas y firmas digitales aplicándolos con herramientas reales.

La [práctica 13](../13-apache-ssl-wireshark) ya genera un certificado autofirmado con OpenSSL. Esta práctica explica las bases que hay detrás.

## 🧰 Herramientas

| Componente | Rol |
|---|---|
| OpenSSL | Hashes, cifrado y certificados |
| GPG | Cifrado y firma de archivos |
| sha256sum | Verificación de integridad |

## ⚙️ Fases previstas

1. Calcular y comparar hashes para verificar la integridad de un archivo.
2. Cifrar y descifrar un archivo con una clave simétrica.
3. Generar un par de claves y cifrar con la clave pública.
4. Firmar un archivo con GPG y verificar la firma.
5. Relacionar lo aprendido con el certificado de la práctica 13.

## 📋 Qué documentar

- Hashes de un archivo antes y después de modificarlo
- Archivo cifrado y descifrado
- Firma verificada y firma inválida tras modificar el archivo

## 🛡️ Buenas prácticas

- Usar algoritmos vigentes y claves de longitud adecuada.
- Proteger las claves privadas y verificar siempre las firmas.

---
> ⚠️ Nota: se realiza únicamente en un entorno de laboratorio aislado propio (VirtualBox), con fines educativos.
