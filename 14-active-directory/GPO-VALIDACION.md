# Aplicar y comprobar una GPO de laboratorio

**Estado: plan preparado, no ejecutado.** Objetivo: demostrar que una política de auditoría se aplica a un equipo de prueba y produce registros útiles para investigación.

## Alcance y reversión

Usar un cliente Windows compatible con las políticas elegidas, dentro de una OU nueva `SOC-Lab`. No vincular la prueba a todo el dominio ni a la OU de controladores. Registrar snapshot, membresía original y estado de auditoría antes de cambiarlo. Mantener una cuenta administrativa de recuperación disponible por consola.

## Procedimiento

1. Crear la OU de prueba y mover únicamente el objeto del cliente designado. Crear una GPO `SOC-Lab-Audit-Logon` vinculada a esa OU.
2. En configuración de equipo, políticas, configuración de Windows, configuración de seguridad, configuración avanzada de directiva de auditoría, inicio/cierre de sesión: habilitar auditoría de inicio de sesión con éxitos y errores. Revisar también la opción que fuerza subcategorías de auditoría frente a categorías heredadas y posibles políticas en conflicto.
3. En el cliente ejecutar `gpupdate /force`; registrar si requiere reinicio. Obtener `gpresult /h gpo-result.html` y `auditpol /get /category:*` con privilegios apropiados.
4. Confirmar que la GPO aparece aplicada y que la subcategoría efectiva es la esperada. Una captura del editor de GPO no demuestra aplicación en el cliente.
5. Con una cuenta de laboratorio no privilegiada, realizar un inicio de sesión correcto y un error controlado. Revisar antes la política de bloqueo y detener la prueba antes de alcanzar su umbral.
6. Buscar eventos en Security del equipo donde ocurrió el intento, no asumir que todo aparece en el DC. Registrar hora, equipo, Event ID, LogonType, cuenta, estado/subestado y correlación con la acción.
7. Exportar evidencia seleccionada, revisada para publicación. Desvincular la GPO y restaurar pertenencia/política inicial al terminar; comprobar estado efectivo, ya que retirar una GPO no garantiza revertir cada ajuste.

## Criterios de aceptación

| Comprobación | Evidencia requerida | Estado |
|---|---|---|
| Alcance limitado | OU y vínculo de GPO | Pendiente |
| Política efectiva | gpresult + auditpol | Pendiente |
| Actividad trazable | Evento y hora de acción coincidentes | Pendiente |
| Reversión | Estado final comparado con el inicial | Pendiente |

[Microsoft: evento 4625 y equipo donde se genera](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) · [Continuar con Wazuh](../16-siem-wazuh/README.md)
