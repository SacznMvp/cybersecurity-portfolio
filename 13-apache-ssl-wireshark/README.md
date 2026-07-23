# Práctica 13 — Montaje y Configuración de Apache II: Cifrado SSL y Análisis de Tráfico
 
## 📌 Objetivo
 
Configurar el cifrado SSL en el servidor web Apache y analizar mediante **curl** y **Wireshark** el tráfico intercambiado entre cliente y servidor, tanto en escenario cifrado (HTTPS) como sin cifrar (HTTP), evidenciando el impacto real de operar sin TLS.
 
## 🧰 Stack y herramientas
 
| Componente | Rol |
|---|---|
| Ubuntu 24 (VirtualBox) | Servidor Apache |
| OpenSSL | Generación del certificado autofirmado |
| Apache (mod_ssl) | Servicio HTTPS en el dominio `sacznweb.local` |
| curl | Inspección del handshake TLS a nivel de aplicación |
| Wireshark 4.2.2 | Captura y análisis de tráfico a nivel de paquete |
 
## ⚙️ Metodología
 
1. **Generación del certificado autofirmado** — par clave/certificado RSA de 2048 bits con OpenSSL, CN=`sacznweb.local`.
2. **Configuración del VirtualHost SSL** — habilitación de módulos `ssl` y `headers`, VirtualHost en el puerto 443.
3. **Verificación en navegador** — confirmación de advertencia esperada por certificado autofirmado y carga correcta del sitio sobre HTTPS.
4. **Análisis con curl** — inspección del handshake TLS: cipher suite, subject/issuer del certificado, fechas de validez.
5. **Análisis con Wireshark** — captura comparativa de tráfico HTTPS (puerto 443) vs. HTTP sin cifrar (puerto 80).
## 🔍 Hallazgos clave
 
- **Tráfico HTTPS (443):** el handshake TLS completo es visible (Client Hello con SNI, Server Hello), pero el contenido de la aplicación viaja como *Application Data* completamente cifrado e ilegible.
- **Tráfico HTTP (80):** las peticiones y respuestas viajan en texto plano — el `GET / HTTP/1.1` y sus cabeceras son perfectamente legibles para cualquiera con acceso a la red.
- **Certificado autofirmado:** subject e issuer coinciden (self-signed), válido por un año — adecuado para laboratorio, pero requeriría una CA pública (ej. Let's Encrypt) en producción.
## ⚠️ Consecuencias de operar sin cifrado
 
| Riesgo | Descripción |
|---|---|
| Robo de credenciales | Formularios de login por HTTP exponen usuario/contraseña en texto plano |
| Session hijacking | Cookies de sesión capturables e inyectables para suplantar al usuario |
| Inyección de contenido | Un atacante en la red puede modificar respuestas HTTP en tránsito |
| Exposición de metadata | Headers HTTP revelan SO, navegador y comportamiento del usuario |
 
## 🧩 Conclusiones
 
La comparación directa entre tráfico cifrado y sin cifrar deja en evidencia por qué HTTPS es un requisito no negociable para cualquier servicio que maneje datos de usuarios. El cifrado SSL/TLS garantiza confidencialidad, integridad y autenticación — sin él, cualquier observador en la red puede leer, capturar o modificar las comunicaciones con herramientas de uso común como Wireshark.
 
## 🗂️ Contenido de esta carpeta
 
- `informe-practica13.pdf` — informe completo (metodología, 14 capturas del proceso y conclusiones)
---
> ⚠️ Nota: laboratorio realizado en un entorno aislado (VirtualBox), sobre el dominio ficticio `sacznweb.local` con certificado autofirmado, con fines exclusivamente educativos.
