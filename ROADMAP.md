# Ruta de aprendizaje

[Volver al portafolio](README.md)



Ruta de aprendizaje por nivel de dificultad: **6 laboratorios con informe y 13 planificados**. Las prácticas 10–14 están enlazadas en la portada; la tabla mantiene la práctica 17 para mostrar su avance de planificada a documentada. Las guías pendientes no equivalen a prácticas realizadas.

| # | Tema | Nivel | Estado |
|---|---|---|---|
| 1 | [Laboratorio virtual con VirtualBox y Kali](./01-laboratorio-virtual) | 🟢 | Planificada · base ya visible en la práctica 14 |
| 2 | [Linux: línea de comandos y permisos](./02-linux-cli-permisos) | 🟢 | Planificada |
| 3 | [Redes y análisis de paquetes](./03-redes-wireshark-tcpdump) | 🟢 | Planificada · Wireshark ya usado en la práctica 13 |
| 4 | [Reconocimiento con Nmap](./04-nmap-reconocimiento) | 🟡 | Planificada · Nmap ya usado en la práctica 11 |
| 5 | [Firewall con iptables y ufw](./05-firewall-iptables-ufw) | 🟡 | Planificada |
| 6 | Cracking de contraseñas (Hashcat, John the Ripper) | 🟡 | Planificada |
| 7 | [Criptografía con OpenSSL y GPG](./07-criptografia-openssl-gpg) | 🟡 | Planificada · OpenSSL ya usado en la práctica 13 |
| 8 | Escaneo de vulnerabilidades (OpenVAS) | 🟠 | Planificada |
| 9 | Explotación guiada con Metasploit | 🔴 | Planificada |
| 15 | [Ataque y defensa sobre Active Directory](./15-ad-ataque-defensa) | 🔴 | Planificada · continúa la práctica 14 |
| 16 | [SIEM con Wazuh](16-siem-wazuh/README.md) | 🟠 | Planificada · guía de recogida y triaje preparada |
| 17 | [Escalada de privilegios en Linux](17-linux-privesc/README.md) | 🟠 | Documentada · tres vías en Metasploitable 2; remediación y retest pendientes |
| 18 | Forense y respuesta a incidentes (Autopsy, Volatility) | 🔴 | Planificada |
| 19 | IDS con Suricata | 🟠 | Planificada |


## Prioridad SOC / Blue Team

1. Completar fundamentos de Linux, redes y firewall (prácticas 1–5).
2. [Detección con Wazuh](16-siem-wazuh/README.md): recoger eventos y validar una alerta con actividad controlada.
3. [Analizador de logs](tools/apache-log-analyzer/README.md): ejecutar con logs del laboratorio y explicar límites y falsos positivos.
4. [Hardening y recuperación de Apache](12-apache-vhost/VALIDACION.md): comparar antes/después y probar una restauración en una VM desechable.
5. [Ataque y defensa AD](15-ad-ataque-defensa/README.md): avanzar cuando la telemetría y los fundamentos estén comprobados.

Los seis informes corresponden a las prácticas 10–14 y 17. El informe de escalada de privilegios en Linux corresponde a la práctica 17. Las guías sin ejecución documentada no aumentan este total. El analizador es una herramienta adicional, fuera de la numeración original de 19 prácticas.

## Criterio para marcar una práctica como completada

- Entorno, versiones y fecha registrados.
- Procedimiento ejecutado y evidencia real enlazada.
- Resultado observado separado del esperado.
- Limitaciones, falsos positivos y medidas de mejora explicados.
- Si se propone una corrección, retest documentado o marcado explícitamente como pendiente.
