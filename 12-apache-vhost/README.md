# Práctica 12 — Montaje y Despliegue de un Servidor Web Apache
 
## 📌 Objetivo
 
Montar y desplegar un servidor web Apache HTTP Server sobre una máquina virtual Ubuntu, configurando un sitio propio mediante Virtual Hosts, corrigiendo advertencias de configuración, y definiendo una estrategia razonada de copias de seguridad y restauración.
 
## 🧰 Stack y herramientas
 
| Componente | Rol |
|---|---|
| Ubuntu Server (VirtualBox) | Sistema base del servidor |
| Apache HTTP Server 2.4 | Servicio web |
| Virtual Hosts | Alojamiento de sitio propio (`sacznweb.local`) |
 
## ⚙️ Metodología
 
1. **Instalación de Apache** — vía APT, verificación de versión y estado del servicio.
2. **Configuración de sitio propio** — creación del `DocumentRoot`, permisos y contenido inicial.
3. **Virtual Host** — fichero de configuración dedicado con `ServerName`, logs y bloque de permisos independientes.
4. **Corrección de advertencias** — resolución del aviso `AH00558` (FQDN) y configuración de resolución local del dominio vía `/etc/hosts`.
5. **Verificación final** — carga exitosa del sitio propio en lugar de la página por defecto.
6. **Estrategia de backups** — análisis razonado de qué respaldar y cómo, ante la ausencia de un módulo nativo de Apache para ello.
## 🔍 Hallazgos clave
 
- Apache en Ubuntu se instala, arranca y se habilita automáticamente — a diferencia de Kali Linux, donde requiere activación manual del servicio.
- La advertencia `AH00558` (FQDN no determinado) se resuelve declarando `ServerName` a nivel global en `apache2.conf`.
- **Apache no incluye ningún módulo nativo de backups** — la copia de seguridad es responsabilidad de administración de sistemas, no del propio software.
## 💾 Estrategia de copias de seguridad
 
| Elemento | Ubicación | Herramienta |
|---|---|---|
| Configuración de Apache | `/etc/apache2/` | `tar`, `rsync`, git |
| Contenido web | `/var/www/` | `tar`, `rsync` |
| Certificados SSL/TLS | `/etc/ssl/`, `/etc/letsencrypt/` | `tar`, `rsync` |
| Logs | `/var/log/apache2/` | `logrotate` + copia periódica |
 
**Buenas prácticas aplicadas:** regla 3-2-1 de backups, versionado de configuración con git, verificación de sintaxis (`apache2ctl configtest`) tras cada restauración, y automatización con `cron`.
 
## 🧩 Conclusiones
 
El despliegue de un servidor Apache va más allá de la instalación: requiere configurar Virtual Hosts correctamente, resolver advertencias de forma metódica, y — un aspecto frecuentemente pasado por alto — diseñar una estrategia de backups propia, ya que Apache no ofrece esta funcionalidad de forma nativa.
 
## 🗂️ Contenido de esta carpeta
 
- `informe-practica12.pdf` — informe completo (metodología, 7 capturas del proceso y estrategia de backups)
---
> ⚠️ Nota: laboratorio realizado en un entorno aislado (VirtualBox), sobre el dominio ficticio `sacznweb.local`, con fines exclusivamente educativos.
