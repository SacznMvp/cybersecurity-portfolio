# Práctica 5 — Firewall con iptables y ufw

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados y el informe se agregarán cuando el laboratorio esté hecho.

| Nivel | Requisitos previos |
|---|---|
| 🟡 Intermedio | Prácticas 2 a 4 |

## 📌 Objetivo

Configurar reglas de firewall en Linux y comprobar, con un escaneo desde otra máquina, el efecto real de cada regla.

Complementa la [práctica 4](../04-nmap-reconocimiento): el mismo escaneo se hace antes y después de aplicar las reglas.

## 🧰 Herramientas

| Componente | Rol |
|---|---|
| ufw | Interfaz sencilla del firewall |
| iptables | Reglas detalladas |
| Nmap | Verificación desde otra máquina |

## ⚙️ Fases previstas

1. Hacer un escaneo previo para tener una línea base.
2. Definir la política por defecto de denegar la entrada y permitir solo lo necesario.
3. Crear las reglas con `ufw` y su equivalente en `iptables`.
4. Registrar los paquetes bloqueados.
5. Repetir el escaneo, comparar y hacer persistentes las reglas.

## 📋 Qué documentar

- Escaneo antes y después
- Listado de reglas aplicadas
- Registros de paquetes bloqueados

## 🛡️ Buenas prácticas

- Denegar por defecto y abrir solo lo imprescindible.
- Probar siempre las reglas desde fuera para confirmar que hacen lo esperado.

---
> ⚠️ Nota: se realiza únicamente en un entorno de laboratorio aislado propio (VirtualBox), con fines educativos.
