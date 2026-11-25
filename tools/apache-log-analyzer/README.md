# Analizador offline de logs Apache

Herramienta Python para practicar triaje de registros Common/Combined. Lee un archivo, cuenta estados, rutas e IP y señala clientes que superan un umbral de respuestas 4xx/5xx. No hace solicitudes de red ni cambia el servidor.

**Estado:** implementación con pruebas automatizadas y muestra sintética. Validación con registros reales del laboratorio pendiente. Python 3.10 o superior, sin paquetes externos.

## Ejecutar desde la raíz del repositorio

```sh
python tools/apache-log-analyzer/analyze.py tools/apache-log-analyzer/sample.log --threshold 3
python tools/apache-log-analyzer/analyze.py tools/apache-log-analyzer/sample.log --threshold 3 --format csv --output triage.csv
python -m unittest discover -s tools/apache-log-analyzer -p "test_*.py" -v
```

El JSON contiene métricas y limitaciones. El CSV contiene únicamente los clientes señalados; el conteo de líneas aceptadas/rechazadas se escribe en stderr. Los archivos de salida deben ser nuevos; el script no los sobrescribe.

## Ejemplo verificable

`sample.log` es completamente sintético y usa direcciones de documentación. Contiene siete líneas: seis válidas y una malformada. Con umbral 3, `192.0.2.20` queda señalado por tres respuestas 4xx. La suma de bytes conocidos es 1088; una solicitud no informa tamaño. Las query strings no se incluyen en las rutas del reporte.

## Interpretación SOC

Revisar si los errores se concentran en un intervalo, si hay despliegues fallidos, clientes legítimos, monitores o proxies. Correlacionar con autenticación y logs de error antes de concluir que hay actividad maliciosa. La muestra no representa un incidente.

Limitaciones: sin ventanas temporales ni lectura de POST; una IP puede agrupar usuarios detrás de NAT; no admite formatos personalizados, nombres DNS en lugar de IP ni rotación automática. Se procesa línea a línea, pero los contadores crecen con las IP/rutas únicas. Las rutas e IP aún pueden ser sensibles: revisar antes de publicar un reporte.

## Próxima validación

- Exportar una muestra de access log del laboratorio y revisar los datos publicables.
- Comparar manualmente conteos de estados con el reporte.
- Documentar un falso positivo y una mejora del criterio de triaje.

[Volver al portafolio](../../README.md)
