# Práctica 2 — Línea de Comandos de Linux y Permisos

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados y el informe se agregarán cuando el laboratorio esté hecho.

| Nivel | Requisitos previos |
|---|---|
| 🟢 Básico | Práctica 1 |

## 📌 Objetivo

Dominar la terminal de Linux y el modelo de usuarios, grupos y permisos, base para entender el hardening y la escalada de privilegios.

Los permisos y la gestión de archivos aparecen de forma implícita en las prácticas [12](../12-apache-vhost) y [13](../13-apache-ssl-wireshark) (directorios, propietarios, `sudo`). Aquí se estudian de forma ordenada.

## 🧰 Herramientas

| Componente | Rol |
|---|---|
| Ubuntu / Kali Linux | Entorno de práctica |
| Bash | Línea de comandos |
| chmod, chown, umask, sudo | Gestión de permisos |

## ⚙️ Fases previstas

1. Navegar por el sistema de archivos y manipular archivos y directorios.
2. Crear usuarios y grupos; revisar `/etc/passwd`, `/etc/group` y la configuración de `sudo`.
3. Cambiar permisos en notación simbólica y octal; cambiar propietario; entender `umask`.
4. Identificar archivos con permisos de riesgo (bit SUID/SGID, escritura para todos) y explicar por qué lo son.
5. Revisar los registros de autenticación en `/var/log` tras iniciar sesión con credenciales erróneas.

## 📋 Qué documentar

- Permisos antes y después de cada cambio
- Hallazgos de permisos de riesgo y su explicación
- Entradas relevantes de los registros

## 🛡️ Buenas prácticas

- Mínimo privilegio: cada usuario y servicio con los permisos justos.
- Revisar periódicamente archivos con permisos excesivos.

---
> ⚠️ Nota: se realiza únicamente en un entorno de laboratorio aislado propio (VirtualBox), con fines educativos.
