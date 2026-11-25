# Validación de las mejoras

Fecha: 2026-11-24.

## Comprobaciones locales

- Analizador Apache: 7 pruebas superadas (fixture conocida, IPv6, campos escapados, entradas inválidas, CSV, CLI y prevención de sobrescritura).
- Backup: 5 pruebas superadas (contenido/hashes, restauración del archivo de prueba en staging, prevención de sobrescritura, fuentes inválidas y destino fuera de fuentes).
- Backup: 2 pruebas de enlaces simbólicos omitidas porque Windows no permite crearlos con los privilegios de esta sesión. Se incluyen en el workflow Linux para comprobarlas cuando pueda publicarse la rama.
- Enlaces locales Markdown: comprobados con `tools/check_links.py`. No valida URLs externas ni anclas.
- Capturas extraídas: revisión visual de las 15 imágenes frente a los informes de origen.
- `git diff --check`: sin errores de espacios.

## Límites

No se ejecutaron Apache, Wazuh, Active Directory ni las nuevas configuraciones en las VMs. La restauración automatizada probada usa archivos temporales, no un servidor operativo. No se afirma validación Linux ni ejecución de GitHub Actions mientras no exista una ejecución confirmada.

La publicación de la rama se intentó, pero el conector devolvió HTTP 403 (Resource not accessible by integration) y Git local no disponía de credenciales para push. Los cambios están guardados localmente.
