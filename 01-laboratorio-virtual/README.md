# 01 · Laboratorio virtual con VirtualBox y Kali Linux

**Estado: práctica documentada** · **Fecha:** 25 de noviembre de 2026

[Volver al portafolio](../README.md) · [Registro de restauración](assets/restauracion.txt)

## Qué se comprobó

Se arrancó Kali Linux en una copia de trabajo creada desde una instantánea existente. Se configuró una red interna dedicada en VirtualBox y se verificó que restaurar una instantánea recuperara la configuración anterior de RAM.

| Componente | Configuración comprobada |
|---|---|
| Hipervisor | Oracle VirtualBox 7.2.8 |
| Máquina de trabajo | SACZN-Practica01-Kali |
| Recursos | 4 CPU virtuales y 4096 MiB de RAM |
| Red | Adaptador 1 en la red interna SACZN-Practica01-Aislada y adaptadores 2–8 deshabilitados |
| Integración | Guest Additions 7.2.4. Portapapeles y arrastrar y soltar deshabilitados |

## Prueba de restauración

1. Con la copia apagada, se creó la instantánea `P01-Base-4096MiB`.
2. Se cambió la memoria de la copia a **3072 MiB** y se comprobó el valor.
3. Al restaurar la instantánea, VirtualBox volvió a mostrar **4096 MiB**. Kali arrancó después de la restauración.

El [registro de arranque](assets/arranque.txt) recoge la versión de Guest Additions notificada por la VM y la versión del kernel informada por el invitado.

El [registro](assets/restauracion.txt) contiene los valores observados antes y después. La prueba comprueba la restauración de la configuración de la VM. El aislamiento se verificó en la configuración de adaptadores de VirtualBox. Queda pendiente comprobar las rutas y la conectividad desde el sistema invitado.

La práctica reutiliza una copia enlazada de Kali que depende de la instantánea de origen. El despliegue de varias máquinas en otra red interna se documenta en la [práctica de Active Directory](../14-active-directory/README.md).
