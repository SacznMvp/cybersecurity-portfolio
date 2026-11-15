# Práctica 1 — Laboratorio Virtual con VirtualBox y Kali Linux

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados y el informe se agregarán cuando el laboratorio esté hecho.

| Nivel | Requisitos previos |
|---|---|
| 🟢 Básico | — |

## 📌 Objetivo

Documentar el laboratorio base que se reutiliza en todas las prácticas: máquina atacante, red interna aislada y snapshots.

La creación de máquinas virtuales y de la red interna `SacznRed` ya aparece, paso a paso, en la [práctica 14](../14-active-directory). Esta práctica la separa y la explica como base general.

## 🧰 Herramientas

| Componente | Rol |
|---|---|
| VirtualBox | Virtualización |
| Kali Linux | Máquina atacante |
| Red interna de VirtualBox | Aislamiento del laboratorio |

## ⚙️ Fases previstas

1. Instalar VirtualBox y comprobar que la virtualización está activa en la BIOS/UEFI.
2. Crear la máquina virtual de Kali Linux desde su ISO y actualizar el sistema.
3. Crear una red interna aislada, asignar direccionamiento y comprobar que no tiene salida a redes reales.
4. Instalar los Guest Additions para integrar portapapeles y pantalla.
5. Crear un snapshot limpio y practicar la restauración.

## 📋 Qué documentar

- Configuración de cada VM (RAM, CPU, disco, red)
- Inventario de máquinas del laboratorio
- Lista de snapshots y prueba de restauración

## 🛡️ Buenas prácticas

- Aislar siempre el laboratorio de redes de producción.
- Usar snapshots para repetir pruebas sin reinstalar.

---
> ⚠️ Nota: se realiza únicamente en un entorno de laboratorio aislado propio (VirtualBox), con fines educativos.
