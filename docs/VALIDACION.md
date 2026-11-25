# Validación de las mejoras


Fecha de validación local: 2026-11-24. Publicación: 2026-11-25.


## Comprobaciones locales


- Analizador Apache: 7 pruebas superadas (fixture conocida, IPv6, campos escapados, entradas inválidas, CSV, CLI y prevención de sobrescritura).
- Backup: 5 pruebas superadas (contenido/hashes, restauración del archivo de prueba en staging, prevención de sobrescritura, fuentes inválidas y destino fuera de fuentes).
- Backup: 2 pruebas de enlaces simbólicos omitidas porque Windows no permite crearlos con los privilegios de esta sesión. Estas pruebas también están incluidas en el workflow Linux.
- Enlaces locales Markdown: comprobados con `tools/check_links.py`. No valida URLs externas ni anclas.
- Capturas extraídas: revisión visual de las 15 imágenes frente a los informes de origen.
- `git diff --check`: sin errores de espacios.


## Límites


No se ejecutaron Apache, Wazuh, Active Directory ni las nuevas configuraciones en las VMs. La restauración automatizada probada usa archivos temporales, no un servidor operativo.


## Publicación y validación automática

Las mejoras están publicadas en la rama `codex/portfolio-profesional`. El workflow de pruebas Python y enlaces Markdown terminó correctamente en GitHub Actions sobre el commit `c84bd90`.

[Ejecución verificada de Portfolio checks](https://github.com/SacznMvp/cybersecurity-portfolio/actions/runs/45551931890).

La comparación con los archivos preparados localmente solo mostró diferencias de finales de línea en LICENSE y sample.log; no hubo diferencias de contenido.

