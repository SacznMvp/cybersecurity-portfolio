# SACZN | Portafolio de ciberseguridad

**SOC / Blue Team · Análisis de registros · Redes · Windows y Linux**

[English](README.en.md) · [Ruta de aprendizaje](ROADMAP.md) · [GitHub](https://github.com/SacznMvp) · [YouTube](https://www.youtube.com/@SACZNCybersecurity)

Soy estudiante de ciberseguridad y desarrollo laboratorios para comprender cómo funcionan los sistemas, reconocer riesgos y documentar su defensa. Mi objetivo profesional es incorporarme a un equipo SOC / Blue Team.

**Portafolio:** 7 casos con informe · 1 guía de entorno · 11 prácticas planificadas.

## Casos destacados para SOC

| Caso | Qué puedes revisar |
|---|---|
| [14 · Active Directory](14-active-directory/README.md) | Dominio, DNS y sesiones verificadas. El caso enlaza la ampliación de auditoría y GPO. |
| [13 · TLS y Wireshark](13-apache-ssl-wireshark/README.md) | Capturas comparables de HTTP y HTTPS y análisis de visibilidad. |
| [16 · Investigación SOC con Wazuh](16-siem-wazuh/README.md) | Evento de sudo en Linux, alerta 5402 y verificación en el indexador. Agente Windows pendiente. |
| [17 · Permisos y privilegios en Linux](17-linux-privesc/README.md) | Evidencias de UID y EUID y controles defensivos pendientes de validar. |

## Otros informes

- [11 · Seguridad web con OWASP Juice Shop](11-owasp-juice-shop/README.md).
- [10 · Análisis estático de Android](10-android-reversing/README.md).
- [12 · Operación y recuperación de Apache](12-apache-vhost/README.md). Despliegue documentado y herramientas disponibles. La restauración en la VM sigue pendiente.

## Herramientas Python

- [Analizador de logs Apache](tools/apache-log-analyzer/README.md): herramienta offline con muestra sintética, JSON/CSV y pruebas automatizadas. Sus indicadores orientan el triaje; no confirman ataques.
- [Backup de configuración y contenido](tools/apache-backup/README.md): archivo de copia con inventario y hashes; prueba de restauración real pendiente.

## Pendiente de ejecutar o validar

- [GPO de Active Directory](14-active-directory/GPO-VALIDACION.md) y [configuración segura de Apache](12-apache-vhost/VALIDACION.md): planes de validación en máquinas virtuales.
- [Ruta de aprendizaje](ROADMAP.md): lista completa de prácticas pendientes.

## Material de apoyo

- [Práctica 1 · Entorno VirtualBox y Kali](01-laboratorio-virtual/README.md). Configuración base e instantáneas. La prueba de red está pendiente.

Las prácticas se realizan en entornos propios de laboratorio. Direcciones privadas, cuentas y tokens visibles en las capturas pertenecen a esas prácticas. La herramienta Python no necesita conectarse a sistemas externos.

Contenido bajo licencia [MIT](LICENSE).
