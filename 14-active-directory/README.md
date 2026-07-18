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
| Active Directory Domain Services | Gestión de identidades y políticas |

## 🌐 Topología
            ┌─────────────────────────┐
            │   Windows Server 2016   │
            │   Controlador de Dominio│
            │      dominio.local      │
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
4. **Gestión de usuarios y políticas** — creación de unidades organizativas (OU), usuarios y aplicación de directivas de grupo (GPO) básicas.
5. **Validación** — verificación de autenticación centralizada desde ambos clientes y revisión de logs del DC.

## 🔍 Hallazgos clave

- La coexistencia de un sistema legado (Windows Server 2003) con un DC moderno (2016) implica retos de compatibilidad de protocolos de autenticación, relevante para entender riesgos en redes corporativas reales que aún mantienen sistemas heredados.
- La gestión centralizada vía AD reduce significativamente la superficie de administración manual, pero también concentra el riesgo: comprometer el DC equivale a comprometer todo el dominio.

## 🗂️ Contenido de esta carpeta

- `informe-practica14.pdf` — informe completo (metodología, capturas y conclusiones)
- `screenshots/` — evidencia visual de cada fase

---
> ⚠️ Nota: todo el entorno fue desplegado en una red aislada de laboratorio (VirtualBox), sin conexión a redes de producción. Usuarios, contraseñas y nombres de dominio son ficticios y usados únicamente con fines educativos.
