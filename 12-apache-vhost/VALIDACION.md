# Plan de hardening y restauración de Apache

**Estado: pendiente de ejecución en VM.** Los resultados de esta tabla son criterios de aceptación, no resultados obtenidos.

## Preparación

Usar una copia desechable de la VM. Registrar fecha, versiones de Ubuntu/Apache/Python, snapshot y configuración inicial. Conservar un acceso por consola. No realizar cambios en producción.

## Comparación antes y después

| Control | Prueba inicial | Cambio propuesto | Aceptación | Observado |
|---|---|---|---|---|
| Listado de directorios | Crear directorio de prueba sin index y solicitarlo | `Options -Indexes` | No se publica el listado; el sitio principal sigue accesible | Pendiente |
| Configuración distribuida | Revisar dependencias de `.htaccess` | `AllowOverride None` si no se utiliza | Funcionalidad conservada y configuración centralizada | Pendiente |
| TLS | Registrar HTTP/HTTPS y confianza | Aplicar [guía TLS](../13-apache-ssl-wireshark/VALIDACION.md) | HTTPS validado sin `-k` | Pendiente |
| Registros | Solicitar una ruta conocida y otra inexistente | Logs separados de acceso y error | Solicitudes localizables por hora, ruta y estado | Pendiente |
| Recuperación | Guardar hashes de config y contenido | Backup y restauración de ensayo | Hashes, configtest y respuesta web correctos | Pendiente |

Tras cada cambio, ejecutar `sudo apache2ctl configtest`. Recargar solo con resultado válido. Si falla la comprobación o la funcionalidad, restaurar la configuración anterior y repetir configtest antes de recargar. No aplicar HSTS al ejercicio comparativo HTTP/HTTPS sin diseñar antes su reversión.

## Ensayo de restauración

1. Generar un backup con el [script](../tools/apache-backup/README.md) sin cambios concurrentes. Conservar su SHA-256 en un lugar separado y protegido.
2. Copiar el archivo a una VM desechable y comparar el hash; revisar `tar -tzf archivo.tar.gz` antes de extraer.
3. Como usuario sin privilegios, extraer una copia propia a un directorio vacío de staging. Si se utiliza Python 3.12+, emplear `tarfile.extractall(..., filter="data")`. Este filtro reduce riesgos, no convierte archivos desconocidos en confiables.
4. Verificar SHA-256 de cada archivo frente a `manifest.json`. Revisar enlaces y permisos; el staging puede aplicar restricciones distintas a los permisos finales.
5. Registrar el estado inicial de la VM destino e instalar manualmente las configuraciones y el DocumentRoot verificados en sus rutas correspondientes, con propietario/permisos adecuados. Asegurar módulos y certificados necesarios; no copiar claves a Git.
6. Ejecutar `apache2ctl configtest`, iniciar o recargar Apache y solicitar el sitio con el encabezado Host correcto. Comparar el contenido con el original y revisar errores.
7. Registrar duración, archivos faltantes, diferencias y resultado final. Ante fallo, volver al snapshot de ensayo y corregir el procedimiento.

## Evidencia que falta publicar

Resumen de hashes (sin secretos), salida de configtest, respuesta HTTP, tiempos de recuperación y captura del sitio restaurado. Añadir una prueba fallida explicada si ocurre. Programar cron y una copia externa solo después de validar la restauración manual.
