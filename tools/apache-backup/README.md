# Backup de Apache para laboratorio

Script Python 3.10+ sin dependencias externas. Empaqueta configuración y DocumentRoot bajo `config/` y `web/`, con un `manifest.json` que contiene SHA-256 de los archivos. No restaura, no borra fuentes y no recarga servicios.

**Estado:** probado con directorios temporales. Recuperación de Apache en una VM pendiente; este script no demuestra que la estrategia 3-2-1 esté implantada.

## Uso en Ubuntu

Crear previamente un directorio privado de backups fuera de las fuentes. Con permisos de lectura suficientes:

```sh
sudo python3 tools/apache-backup/backup.py --config /etc/apache2 --web /var/www/sacznweb --output /var/backups/saczn/apache-2026-11-24.tar.gz
python3 -m unittest discover -s tools/apache-backup -p "test_*.py" -v
```

Usar un nombre nuevo en cada ejecución. El archivo se crea con modo 0600 en POSIX y no se sobrescribe. Puede contener claves privadas o secretos si están en la configuración: mantenerlo fuera de Git y proteger la copia externa. En Windows los permisos dependen de ACL, no del modo POSIX.

Se preservan enlaces relativos internos; se rechazan enlaces absolutos, externos o rotos, archivos especiales, fuentes anidadas y destinos dentro de las fuentes. Si hay certificados fuera de `/etc/apache2`, deben respaldarse por un procedimiento adicional protegido. No incluye bases de datos, logs, ACL, atributos extendidos ni una imagen del sistema.

Detener cambios de configuración/contenido durante la copia: no es un snapshot atómico ni ofrece protección frente a modificaciones concurrentes maliciosas. Los hashes detectan diferencias, no acreditan autenticidad frente a un atacante que pueda sustituir el archivo completo.

## Restauración

Seguir el [procedimiento de validación](../../12-apache-vhost/VALIDACION.md). Inspeccionar el archivo y extraer solo una copia propia y verificada a un directorio vacío de staging en una VM desechable. Comprobar hashes, enlaces y permisos antes de instalar archivos. Nunca extraer directamente sobre `/` como primer paso.
