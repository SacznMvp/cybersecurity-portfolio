# SACZN | Portafolio de ciberseguridad

**SOC / Blue Team junior · Análisis de registros · Redes · Windows y Linux**

[English](README.en.md) · [Ruta de aprendizaje](ROADMAP.md) · [GitHub](https://github.com/SacznMvp) · [YouTube](https://www.youtube.com/@SACZNCybersecurity)

Soy estudiante de ciberseguridad y desarrollo laboratorios para comprender cómo funcionan los sistemas, reconocer riesgos y documentar su defensa. Mi objetivo profesional es incorporarme a un equipo SOC / Blue Team.

**Portafolio:** 6 casos con informe · 1 guía de entorno · 12 prácticas planificadas.

## Laboratorios documentados

| # | Laboratorio | Evidencia y alcance |
|---|---|---|
| 10 | [Android: análisis estático](10-android-reversing/README.md) | APKTool y JADX; observaciones separadas de vulnerabilidades confirmadas |
| 11 | [Seguridad web](11-owasp-juice-shop/README.md) | Reconocimiento y autenticación en una aplicación vulnerable local |
| 12 | [Apache: Virtual Hosts](12-apache-vhost/README.md) | Configuración y sitio funcionando; restauración todavía pendiente |
| 13 | [Apache: TLS y Wireshark](13-apache-ssl-wireshark/README.md) | Capturas HTTP/HTTPS y certificado de laboratorio |
| 14 | [Infraestructura Active Directory](14-active-directory/README.md) | Red interna, dominio, usuarios y clientes |
| 17 | [Escalada de privilegios en Linux](17-linux-privesc/README.md) | SUID, cron y permisos débiles en Metasploitable 2; mitigación y retest pendientes |

Cada laboratorio enlaza a su documentación, evidencias y resultados. Las aclaraciones están en los README y en las [notas de revisión técnica](docs/REVISION-TECNICA.md).

## Herramientas Python

- [Analizador de logs Apache](tools/apache-log-analyzer/README.md): herramienta offline con muestra sintética, JSON/CSV y pruebas automatizadas. Sus indicadores orientan el triaje; no confirman ataques.
- [Backup de configuración y contenido](tools/apache-backup/README.md): archivo de copia con inventario y hashes; prueba de restauración real pendiente.

## Pendiente de ejecutar o validar

- [Wazuh](16-siem-wazuh/README.md): guía preparada. Falta instalar el laboratorio, recoger eventos e investigar una alerta.
- [GPO de Active Directory](14-active-directory/GPO-VALIDACION.md) y [configuración segura de Apache](12-apache-vhost/VALIDACION.md): planes de validación en máquinas virtuales.
- [Ruta de aprendizaje](ROADMAP.md): lista completa de prácticas pendientes.

## Material de apoyo

- [Práctica 1 · Entorno VirtualBox y Kali](01-laboratorio-virtual/README.md). Configuración base e instantáneas. La prueba de red está pendiente.

Las prácticas se realizan en entornos propios de laboratorio. Direcciones privadas, cuentas y tokens visibles en las capturas pertenecen a esas prácticas. La herramienta Python no necesita conectarse a sistemas externos.

Contenido bajo licencia [MIT](LICENSE).
