# 🛡️ Cybersecurity Portfolio — SACZN

🌐 **Español** · [English](./README.en.md)

Laboratorios prácticos de ciberseguridad, desarrollados durante mi formación técnica. Cada carpeta documenta un laboratorio independiente: objetivo, herramientas, metodología, hallazgos, evidencia y lecciones aprendidas.

> **Perfil:** estudiante de ciberseguridad con práctica en auditoría web, seguridad móvil, redes y administración de infraestructura Windows/Linux. Formación orientada a auditoría ofensiva, defensa y respuesta a incidentes.
>
> 📫 **Contacto:** [GitHub @SacznMvp](https://github.com/SacznMvp) · 🎥 [Canal de YouTube](https://www.youtube.com/@SACZNCybersecurity) <!-- TODO: añadir enlace de LinkedIn / correo profesional -->

## 📂 Laboratorios

| # | Práctica | Tecnologías | Categoría |
|---|---|---|---|
| 14 | [Red corporativa con Active Directory](./14-active-directory) | Windows Server 2016/2003, Windows 10, AD DS, VirtualBox | Infraestructura Windows |
| 13 | [Apache II — Cifrado SSL y análisis de tráfico](./13-apache-ssl-wireshark) | Apache, OpenSSL, curl, Wireshark, Ubuntu | Redes y criptografía |
| 12 | [Apache — Virtual Hosts y backups](./12-apache-vhost) | Apache, Ubuntu Server, VirtualBox | Administración de servidores |
| 11 | [Seguridad web — OWASP Juice Shop](./11-owasp-juice-shop) | Nmap, Gobuster, Nikto, Burp Suite, Kali Linux | Pentesting web |
| 10 | [Seguridad móvil en Android — Reversing](./10-android-reversing) | InsecureBankv2, APKTool, JADX-GUI, Kali Linux | Seguridad móvil |

## 🧰 Habilidades demostradas

| Área | Evidencia |
|---|---|
| Pentesting web (OWASP Top 10) | [Práctica 11](./11-owasp-juice-shop): reconocimiento, enumeración, análisis de JWT, SQL injection |
| Seguridad móvil e ingeniería inversa | [Práctica 10](./10-android-reversing): decompilación y análisis estático de APK |
| Análisis de tráfico de red | [Práctica 13](./13-apache-ssl-wireshark): captura y comparación HTTP vs HTTPS en Wireshark |
| TLS y certificados | [Práctica 13](./13-apache-ssl-wireshark): certificado autofirmado con OpenSSL, handshake TLS |
| Administración de servidores web | Prácticas [12](./12-apache-vhost) (Virtual Hosts y backups) y [13](./13-apache-ssl-wireshark) (HTTPS) |
| Active Directory y entornos Windows | [Práctica 14](./14-active-directory): dominio, usuarios, equipos legados |
| Documentación técnica | Informe en PDF por práctica, con metodología y capturas |

## 🗺️ Hoja de ruta

Próximos laboratorios planificados (aún **no** realizados):

| # | Laboratorio | Objetivo |
|---|---|---|
| 15 | Ataque y defensa sobre Active Directory | Enumeración, Kerberoasting, Pass-the-Hash y su detección sobre el dominio de la práctica 14 ([guía](./15-ad-ataque-defensa)) |
| 16 | SIEM con Wazuh | Detectar los ataques de las prácticas 11 y 15 |
| 17 | Escalada de privilegios en Linux | Máquina de práctica guiada y mitigaciones |
| 18 | Forense y respuesta a incidentes | Análisis con Autopsy / Volatility |
| 19 | IDS con Suricata | Detectar escaneos de Nmap y tráfico web malicioso |

## 📌 Sobre este repositorio

Todo el contenido se desarrolla en entornos de laboratorio aislados (VirtualBox), sin conexión a redes de producción. Usuarios, contraseñas y nombres de dominio son ficticios y usados únicamente con fines educativos.

Contenido bajo licencia [MIT](./LICENSE).
