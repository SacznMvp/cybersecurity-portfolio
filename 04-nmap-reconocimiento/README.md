# Práctica 4 — Reconocimiento de Red con Nmap

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados y el informe se agregarán cuando el laboratorio esté hecho.

| Nivel | Requisitos previos |
|---|---|
| 🟡 Intermedio | Prácticas 1 a 3 |

## 📌 Objetivo

Descubrir equipos, puertos y servicios de una red de laboratorio propia y documentar su superficie de exposición.

Nmap ya se usó dentro de la [práctica 11](../11-owasp-juice-shop) contra Juice Shop. Aquí se estudia de forma completa sobre una red interna.

## 🧰 Herramientas

| Componente | Rol |
|---|---|
| Nmap | Descubrimiento de hosts, puertos y servicios |
| Kali Linux | Máquina de trabajo |
| Máquinas virtuales propias del laboratorio | Objetivos en red interna |

## ⚙️ Fases previstas

1. Descubrir qué equipos están activos en la red interna.
2. Identificar puertos abiertos y los servicios y versiones que los atienden.
3. Interpretar los resultados y compararlos con lo que se espera que esté expuesto.
4. Guardar los resultados en distintos formatos para el informe.
5. Revisar, desde el lado del servidor, qué rastro deja un escaneo en los registros.

## 📋 Qué documentar

- Equipos descubiertos
- Tabla de puertos y servicios
- Rastro del escaneo en los registros del servidor

## 🛡️ Buenas prácticas

- Cerrar o filtrar los puertos que no sean necesarios.
- Mantener actualizados los servicios expuestos.

---
> ⚠️ Nota: se realiza únicamente en un entorno de laboratorio aislado propio (VirtualBox), con fines educativos.
