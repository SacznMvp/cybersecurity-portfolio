# Práctica 14 — Despliegue de Red Corporativa con Active Directory

## 📌 Objetivo

Diseñar y desplegar una infraestructura de red corporativa simulada utilizando **Active Directory** sobre un entorno virtualizado, aplicando conceptos de administración de dominios, gestión centralizada de usuarios y coexistencia de sistemas operativos de distintas generaciones dentro de un mismo dominio.

## 🧰 Stack y herramientas

| Componente | Rol |
|---|---|
| VirtualBox | Virtualización de la infraestructura |
| Windows Server 2016 | Controlador de Dominio (DC) |
| Windows 10 | Estación de trabajo cliente |
| Windows Server 2003 | Sistema legado dentro del dominio |
| Active Directory Domain Services | Gestión centralizada de identidades |

## 🌐 Topología
            ┌─────────────────────────┐
            │   Windows Server 2016   │
            │   Controlador de Dominio│
            │       saczn.local       │
            └────────────┬────────────┘
                         │
          ┌──────────────┴──────────────┐
          │                              │
 ┌────────▼────────┐          ┌─────────▼─────────┐
 │   Windows 10     │          │ Windows Server 2003│
 │  Cliente unido    │          │  Sistema legado     │
 │   al dominio       │          │  unido al dominio    │
 └───────────────────┘          └─────────────────────┘

## ⚙️ Fases del laboratorio

1. **Preparación del entorno** — instalación y configuración de red interna en VirtualBox para las tres máquinas virtuales.
2. **Promoción a Controlador de Dominio** — instalación del rol AD DS en Windows Server 2016 y creación del dominio.
3. **Unión de clientes al dominio** — incorporación de Windows 10 y Windows Server 2003, validando compatibilidad y comunicación con el DC.
4. **Gestión de usuarios** — creación de un usuario de dominio desde la consola *Usuarios y equipos de Active Directory*.
5. **Validación** — inicio de sesión con la cuenta de dominio en ambos clientes (`whoami`) y comprobación de los equipos en el contenedor *Computers* del DC.

## 🔍 Hallazgos clave

- Un cliente legado (Windows Server 2003) se une sin problemas a un DC moderno (Windows Server 2016) y autentica con una cuenta de dominio: demuestra la madurez de LDAP/Kerberos.
- Mantener ese tipo de sistemas en producción es un riesgo de seguridad considerable: no reciben soporte ni actualizaciones desde hace más de una década.
- Recomendación del informe: segmentar en una VLAN aislada cualquier equipo legado que deba mantenerse por compatibilidad.

## 🎓 Lecciones aprendidas

- El DNS correcto (el propio DC) es requisito para que un cliente localice el dominio y se una a él.
- Que un sistema legado funcione en el dominio no significa que sea seguro: la compatibilidad no sustituye al soporte y las actualizaciones.
- La autenticación centralizada se verifica en cada cliente: `whoami` devuelve la cuenta de dominio (`saczn\...`).

## ➡️ Siguiente paso

Este entorno es la base para una práctica de ataque y defensa sobre AD (enumeración, Kerberoasting, Pass-the-Hash). Ver la [hoja de ruta](../README.md).

## 🗂️ Contenido de esta carpeta

- `informe-practica14.pdf` — informe completo (metodología, capturas y conclusiones)

---
> ⚠️ Nota: todo el entorno fue desplegado en una red aislada de laboratorio (VirtualBox), sin conexión a redes de producción. Usuarios, contraseñas y nombres de dominio son ficticios y usados únicamente con fines educativos.
