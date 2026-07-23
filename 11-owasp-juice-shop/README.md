# Práctica 11 — Seguridad en Aplicaciones Web (OWASP Juice Shop)
 
## 📌 Objetivo
 
Realizar una auditoría de seguridad completa sobre **OWASP Juice Shop**, una aplicación web deliberadamente vulnerable, aplicando una metodología equivalente a la de un pentest profesional (alineada con OWASP Testing Guide y PTES): reconocimiento, enumeración, análisis de cabeceras y cifrado, análisis de tokens de sesión, y explotación de vulnerabilidades.
 
## 🧰 Stack y herramientas
 
| Componente | Rol |
|---|---|
| Kali Linux | Sistema atacante |
| OWASP Juice Shop (Docker) | Aplicación objetivo |
| Nmap | Escaneo de puertos y servicios |
| Gobuster | Fuzzing de directorios y archivos |
| Nikto | Análisis automatizado de vulnerabilidades web |
| Burp Suite Community Edition | Interceptación, Sequencer, explotación manual |
 
## ⚙️ Metodología
 
1. **Reconocimiento** — escaneo de puertos con Nmap y fingerprinting del servicio.
2. **Enumeración** — fuzzing de directorios con Gobuster, revisión de `robots.txt` y `sitemap.xml`.
3. **Análisis de cabeceras y cifrado** — revisión con curl y Nikto de cabeceras de seguridad y ausencia de TLS.
4. **Análisis de tokens de sesión** — evaluación de entropía de JWT mediante Burp Sequencer.
5. **Explotación** — bypass de autenticación vía credenciales débiles e inyección SQL.
## 🔍 Hallazgos por severidad
 
| Severidad | Hallazgo |
|---|---|
| 🔴 Crítica | Inyección SQL en login con bypass de autenticación (`' OR 1=1--`) |
| 🟠 Alta | Credenciales de administrador débiles/públicas |
| 🟠 Alta | Ausencia total de cifrado de transporte (HTTP sin TLS) |
| 🟡 Media | Directorio `/ftp` expuesto públicamente |
| 🟡 Media | CORS configurado de forma permisiva (`Access-Control-Allow-Origin: *`) |
| 🟡 Media | Cabeceras de seguridad ausentes (CSP, HSTS, Permissions-Policy, Referrer-Policy) |
| 🟢 Baja | `sitemap.xml` mal configurado (sin impacto directo) |
 
## 💡 Vulnerabilidad destacada: Inyección SQL con bypass de autenticación
 
El campo de email del formulario de login no sanea ni parametriza la entrada del usuario. El payload `' OR 1=1--` neutraliza la verificación de contraseña, permitiendo autenticarse como el primer usuario de la base de datos (administrador) sin conocer ninguna credencial real.
 
**Clasificación:** CWE-89 · OWASP Top 10 A03:2021 — Injection
 
**Recomendación:** sustituir la concatenación de cadenas por consultas parametrizadas o un ORM con bind parameters, aplicar validación estricta de entrada, y desplegar un WAF como capa de defensa adicional.
 
## 🗂️ Contenido de esta carpeta
 
- `informe-practica11.pdf` — informe completo (metodología, 13 capturas del proceso, análisis y conclusiones)
---
> ⚠️ Nota: la auditoría se realizó contra una instancia local de OWASP Juice Shop (contenedor Docker en `localhost:3000`), una aplicación oficialmente diseñada por OWASP para practicar pentesting web. Las credenciales y vulnerabilidades documentadas son propias de este entorno de laboratorio público.
 
