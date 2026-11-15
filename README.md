# 🛡️ Cybersecurity Portfolio — SACZN

🌐 **Español** · [English](./README.en.md)

Laboratorios prácticos de ciberseguridad, desarrollados durante mi formación técnica. Cada carpeta documenta un laboratorio independiente: objetivo, herramientas, metodología, hallazgos, evidencia y lecciones aprendidas.

> **Perfil:** estudiante de ciberseguridad con práctica en auditoría web, seguridad móvil, redes y administración de infraestructura Windows/Linux. Formación orientada a auditoría ofensiva, defensa y respuesta a incidentes.
>
> 📫 **Contacto:** [GitHub @SacznMvp](https://github.com/SacznMvp) · 🎥 [Canal de YouTube](https://www.youtube.com/@SACZNCybersecurity) <!-- TODO: añadir enlace de LinkedIn / correo profesional -->

## 📂 Laboratorios realizados

| # | Práctica | Tecnologías | Categoría | Nivel |
|---|---|---|---|---|
| 14 | [Red corporativa con Active Directory](./14-active-directory) | Windows Server 2016/2003, Windows 10, AD DS, VirtualBox | Infraestructura Windows | 🟠 |
| 13 | [Apache II — Cifrado SSL y análisis de tráfico](./13-apache-ssl-wireshark) | Apache, OpenSSL, curl, Wireshark, Ubuntu | Redes y TLS | 🟡 |
| 12 | [Apache — Virtual Hosts y backups](./12-apache-vhost) | Apache, Ubuntu Desktop, VirtualBox | Administración de servidores | 🟢 |
| 11 | [Seguridad web — OWASP Juice Shop](./11-owasp-juice-shop) | Nmap, Gobuster, Nikto, Burp Suite, Kali Linux | Pentesting web | 🟡 |
| 10 | [Seguridad móvil en Android — Reversing](./10-android-reversing) | InsecureBankv2, APKTool, JADX-GUI, Kali Linux | Seguridad móvil | 🟡 |

**Nivel:** 🟢 básico · 🟡 intermedio · 🟠 intermedio-alto · 🔴 avanzado. Es una estimación propia de la dificultad relativa.

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

## 🗺️ Ruta de aprendizaje

Laboratorios planificados, ordenados por nivel de dificultad. Aún **no** están realizados; las guías de trabajo se irán completando con informe propio.

| # | Tema | Nivel | Estado |
|---|---|---|---|
| 1 | [Laboratorio virtual con VirtualBox y Kali](./01-laboratorio-virtual) | 🟢 | Planificada · base ya visible en la práctica 14 |
| 2 | [Linux: línea de comandos y permisos](./02-linux-cli-permisos) | 🟢 | ✅ Realizada |
| 3 | [Redes y análisis de paquetes](./03-redes-wireshark-tcpdump) | 🟢 | ✅ Realizada (con tcpdump, sin Wireshark — ver nota en la práctica) |
| 4 | [Reconocimiento con Nmap](./04-nmap-reconocimiento) | 🟡 | Planificada · Nmap ya usado en la práctica 11 |
| 5 | [Firewall con iptables y ufw](./05-firewall-iptables-ufw) | 🟡 | Planificada |
| 6 | Cracking de contraseñas (Hashcat, John the Ripper) | 🟡 | Planificada |
| 7 | [Criptografía con OpenSSL y GPG](./07-criptografia-openssl-gpg) | 🟡 | Planificada · OpenSSL ya usado en la práctica 13 |
| 8 | Escaneo de vulnerabilidades (OpenVAS) | 🟠 | Planificada |
| 9 | Explotación guiada con Metasploit | 🔴 | Planificada |
| 15 | [Ataque y defensa sobre Active Directory](./15-ad-ataque-defensa) | 🔴 | Planificada · continúa la práctica 14 |
| 16 | SIEM con Wazuh | 🟠 | Planificada · detectar los ataques de las prácticas 11 y 15 |
| 17 | Escalada de privilegios en Linux | 🟠 | Planificada |
| 18 | Forense y respuesta a incidentes (Autopsy, Volatility) | 🔴 | Planificada |
| 19 | IDS con Suricata | 🟠 | Planificada |

## 📌 Sobre este repositorio

Todo el contenido se desarrolla en entornos de laboratorio aislados (VirtualBox), sin conexión a redes de producción. Usuarios, contraseñas y nombres de dominio son ficticios y usados únicamente con fines educativos.

Contenido bajo licencia [MIT](./LICENSE).
