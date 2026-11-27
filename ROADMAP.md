# Ruta de aprendizaje

[Volver al portafolio](README.md)



**19 prácticas · 7 casos con informe · 1 guía de entorno · 11 planificadas.**

## Prácticas con informe

Los informes y sus evidencias se pueden abrir desde la [portada del portafolio](README.md#casos-destacados-para-soc). Corresponden a las prácticas 10–14, 16 y 17. Algunas aún tienen verificaciones pendientes, como la restauración de Apache y las pruebas de remediación en Linux.

La [práctica 1 de VirtualBox y Kali](01-laboratorio-virtual/README.md) documenta el entorno base. Queda como referencia para preparar las máquinas y recuperar instantáneas.

## Temas integrados en casos

| Tema | Caso donde aporta evidencia |
|---|---|
| 02 · Terminal y permisos de Linux | [17 · Permisos y privilegios](17-linux-privesc/README.md) |
| 03 · Captura de red y 07 · Criptografía | [13 · TLS y Wireshark](13-apache-ssl-wireshark/README.md) |
| 04 · Reconocimiento | [11 · Seguridad web](11-owasp-juice-shop/README.md) |
| 05 · Firewall | [12 · Operación de Apache](12-apache-vhost/README.md) |
| 15 · Auditoría de Active Directory | [14 · Active Directory](14-active-directory/README.md) |

La tabla inferior conserva la numeración y los estados originales de los temas pendientes. Las actividades integradas pueden documentarse dentro del informe del caso correspondiente.

## Prácticas pendientes de ejecutar

Una guía preparada describe el trabajo previsto. El resultado se documenta cuando se ejecuta la práctica y se reúne la evidencia.

| # | Tema | Nivel | Estado |
|---|---|---|---|
| 2 | [Linux: línea de comandos y permisos](./02-linux-cli-permisos) | 🟢 | Planificada |
| 3 | [Redes y análisis de paquetes](./03-redes-wireshark-tcpdump) | 🟢 | Planificada · Wireshark ya usado en la práctica 13 |
| 4 | [Reconocimiento con Nmap](./04-nmap-reconocimiento) | 🟡 | Planificada · Nmap ya usado en la práctica 11 |
| 5 | [Firewall con iptables y ufw](./05-firewall-iptables-ufw) | 🟡 | Planificada |
| 6 | Cracking de contraseñas (Hashcat, John the Ripper) | 🟡 | Planificada |
| 7 | [Criptografía con OpenSSL y GPG](./07-criptografia-openssl-gpg) | 🟡 | Planificada · OpenSSL ya usado en la práctica 13 |
| 8 | Escaneo de vulnerabilidades (OpenVAS) | 🟠 | Planificada |
| 9 | Explotación guiada con Metasploit | 🔴 | Planificada |
| 15 | [Ataque y defensa sobre Active Directory](./15-ad-ataque-defensa) | 🔴 | Planificada · continúa la práctica 14 |
| 18 | Forense y respuesta a incidentes (Autopsy, Volatility) | 🔴 | Planificada |
| 19 | IDS con Suricata | 🟠 | Planificada |


## Prioridad SOC / Blue Team

1. [Ampliar Wazuh a Windows](16-siem-wazuh/README.md#ampliación-pendiente--autenticación-de-windows). La alerta inicial de Linux ya está investigada e indexada. Falta correlacionar una alerta con el evento Windows de origen.
2. Aplicar los fundamentos de Linux, redes y firewall (prácticas 2–5) allí donde aporten evidencia a un caso. Por ejemplo, usar permisos y registros de Linux al investigar una alerta, y capturas de red al explicar qué tráfico se observó.
3. [Analizador de logs](tools/apache-log-analyzer/README.md): ejecutar con logs del laboratorio y explicar límites y falsos positivos.
4. [Hardening y recuperación de Apache](12-apache-vhost/VALIDACION.md): comparar antes/después y probar una restauración en una VM desechable.
5. [Ataque y defensa AD](15-ad-ataque-defensa/README.md): avanzar cuando la telemetría y los fundamentos estén comprobados.


## Criterio para marcar una práctica como completada

- Entorno, versiones y fecha registrados.
- Procedimiento ejecutado y evidencia real enlazada.
- Resultado observado separado del esperado.
- Limitaciones, falsos positivos y medidas de mejora explicados.
- Si se propone una corrección, retest documentado o marcado explícitamente como pendiente.
