# SACZN | Portafolio de ciberseguridad

**SOC / Blue Team junior · Análisis de registros · Redes · Windows y Linux**

[English](README.en.md) · [Ruta de aprendizaje](ROADMAP.md) · [GitHub](https://github.com/SacznMvp) · [YouTube](https://www.youtube.com/@SACZNCybersecurity)

Soy estudiante de ciberseguridad y desarrollo laboratorios para comprender cómo funcionan los sistemas, reconocer riesgos y documentar su defensa. Mi objetivo profesional es incorporarme a un equipo SOC / Blue Team junior.

**Estado:** 6 laboratorios con informe · 13 prácticas planificadas en la ruta original · 1 herramienta Python adicional.

## Proyectos destacados

| Proyecto | Resultado documentado | Relevancia para un SOC |
|---|---|---|
| [Active Directory](14-active-directory/README.md) | Dominio, DNS y dos clientes; evidencia de pertenencia y sesión de dominio | Contexto de identidades y autenticación Windows |
| [HTTP frente a HTTPS](13-apache-ssl-wireshark/README.md) | Comparación de tráfico visible y cifrado en Wireshark | Interpretación de tráfico y límites de visibilidad |
| [OWASP Juice Shop](11-owasp-juice-shop/README.md) | Bypass de autenticación documentado y caso de estudio | Comprender ataques para identificar señales defensivas |

## Laboratorios documentados

| # | Laboratorio | Evidencia y alcance |
|---|---|---|
| 10 | [Android: análisis estático](10-android-reversing/README.md) | APKTool y JADX; observaciones separadas de vulnerabilidades confirmadas |
| 11 | [Seguridad web](11-owasp-juice-shop/README.md) | Reconocimiento y autenticación en una aplicación vulnerable local |
| 12 | [Apache: Virtual Hosts](12-apache-vhost/README.md) | Configuración y sitio funcionando; restauración todavía pendiente |
| 13 | [Apache: TLS y Wireshark](13-apache-ssl-wireshark/README.md) | Capturas HTTP/HTTPS y certificado de laboratorio |
| 14 | [Infraestructura Active Directory](14-active-directory/README.md) | Red interna, dominio, usuarios y clientes |
| 17 | [Escalada de privilegios en Linux](17-linux-privesc/README.md) | SUID, cron y permisos débiles en Metasploitable 2; mitigación y retest pendientes |

Cada laboratorio incluye capturas extraídas de su informe original, explicación del resultado y enlace al PDF. Los PDF se conservan como registro histórico; las precisiones técnicas actuales están en los README y en las [notas de revisión](docs/REVISION-TECNICA.md).

## Código y próximos pasos defensivos

- [Analizador de logs Apache](tools/apache-log-analyzer/README.md): herramienta offline con muestra sintética, JSON/CSV y pruebas automatizadas. Sus indicadores orientan el triaje; no confirman ataques.
- [Backup de configuración y contenido](tools/apache-backup/README.md): archivo de copia con inventario y hashes; prueba de restauración real pendiente.
- [Detección con Wazuh](16-siem-wazuh/README.md): guía preparada para generar, recoger e investigar eventos. Laboratorio pendiente.
- [Validación de GPO](14-active-directory/GPO-VALIDACION.md) y [hardening Apache](12-apache-vhost/VALIDACION.md): planes de ejecución con criterios verificables.

## Cómo leer la evidencia

**Documentado** significa que existe evidencia en el informe. **Propuesto** significa que hay código o una guía para probar. **Pendiente** significa que falta ejecutar o validar el resultado en las máquinas virtuales. No se presentan simulaciones ni datos sintéticos como incidentes reales.

Las prácticas se realizan en entornos propios de laboratorio. Direcciones privadas, cuentas y tokens visibles en las capturas pertenecen a esas prácticas. La herramienta Python no necesita conectarse a sistemas externos.

Contenido bajo licencia [MIT](LICENSE).
