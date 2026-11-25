# Revisión técnica de la documentación

Fecha: 2026-11-24. Los PDF originales se conservan sin alteración como entregas históricas. Esta revisión actualiza la interpretación; no registra una nueva ejecución de los laboratorios.

| Práctica | Precisión |
|---|---|
| Android | Imports, clases legibles y nombre de preferencias no prueban por sí solos exposición de credenciales o escalada. La referencia a EncryptedSharedPreferences está deprecada. |
| Juice Shop | Evaluación de alcance limitado. CORS, cabeceras, rutas públicas y errores 500 requieren demostrar impacto antes de asignar severidad. Sequencer no valida criptográficamente JWT, ni siquiera aislando la firma. |
| Apache | La estrategia de backup es propuesta, no aplicada. El cron histórico contiene `%` que requiere escape en crontab; usar un script evita ese problema. |
| TLS | Parte del handshake TLS 1.3 está cifrada. `curl -k` no verifica confianza; SAN y una confianza explícita permiten una prueba mejor. SNI visible describe la captura, no todas las conexiones. |
| AD | Windows 10 muestra administrador; el usuario estándar aparece en el cliente legado. La unión de equipos no prueba el protocolo utilizado ni una GPO efectiva. |

Las configuraciones nuevas están identificadas como transcritas o propuestas. Las imágenes proceden de los PDF ya publicados y su nombre contiene la página de origen (base 1). Los datos sintéticos del analizador están identificados como tales.

## Pendientes que requieren intervención del autor

- Ejecutar las ampliaciones en las máquinas virtuales y registrar versiones, fecha y resultados.
- Probar restauración, GPO y alertas; publicar evidencia de éxito y fallos, sin completar por anticipado.
- Confirmar datos de contacto profesionales cuando estén actualizados. Se mantienen GitHub y YouTube.
- Traducir los informes individuales si se desea una candidatura completamente bilingüe; la portada inglesa no equivale a informes traducidos.
