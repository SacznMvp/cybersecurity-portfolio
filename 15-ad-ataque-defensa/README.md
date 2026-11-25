# Práctica 15 — Ataque y Defensa sobre Active Directory

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados, capturas e informe se agregarán al completar el laboratorio.

| Nivel | Requisitos previos |
|---|---|
| 🔴 Avanzado | Práctica 14 y prácticas 1 a 5 |

## 📌 Objetivo

Atacar el dominio `saczn.local` desplegado en la [práctica 14](../14-active-directory) con técnicas comunes de post-explotación en Active Directory, y documentar para cada una cómo se detecta y cómo se mitiga.

## 🧰 Stack previsto

| Componente | Rol |
|---|---|
| Entorno de la práctica 14 | Dominio objetivo (DC Windows Server 2016 + clientes) |
| Kali Linux | Máquina atacante en la misma red interna |
| BloodHound + SharpHound | Mapeo de relaciones y rutas de ataque |
| Impacket | Kerberoasting, Pass-the-Hash |
| Hashcat | Cracking offline de hashes obtenidos |

## ⚙️ Fases previstas

1. **Preparación** — agregar Kali a la red interna `SacznRed`; crear cuentas de servicio con SPN y contraseñas de prueba débiles.
2. **Enumeración** — usuarios, grupos y equipos del dominio; mapeo con BloodHound.
3. **Kerberoasting** — solicitar tickets de servicio y crackear el hash offline.
4. **Pass-the-Hash** — movimiento lateral con un hash NTLM obtenido en el laboratorio.
5. **Detección** — revisar 4769 en el DC y 4624/4625 en el equipo correspondiente al inicio de sesión, según la auditoría habilitada. Correlacionar campos y contexto; un evento aislado no confirma una técnica. Preparar primero la [recogida y validación de eventos](../16-siem-wazuh/README.md).
6. **Mitigación** — contraseñas largas en cuentas de servicio o gMSA, deshabilitar NTLM donde sea posible, modelo de administración por niveles.

## 📋 Plantilla del informe

- Objetivo y alcance
- Topología y direccionamiento
- Procedimiento por técnica, con capturas
- Hallazgos por severidad
- Detección (eventos y firmas)
- Mitigación
- Lecciones aprendidas

---
> ⚠️ Nota: todas las técnicas se ejecutan únicamente sobre el entorno aislado de laboratorio propio (VirtualBox), con fines educativos.
