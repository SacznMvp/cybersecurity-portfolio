# Práctica 3 — Fundamentos de Redes y Análisis de Paquetes

> 🚧 **Estado: planificada.** Esta carpeta es la guía de trabajo; los resultados y el informe se agregarán cuando el laboratorio esté hecho.

| Nivel | Requisitos previos |
|---|---|
| 🟢 Básico | Prácticas 1 y 2 |

## 📌 Objetivo

Entender cómo viajan los datos (ARP, ICMP, DNS, TCP) capturando y leyendo tráfico real del laboratorio.

La [práctica 13](../13-apache-ssl-wireshark) ya usa Wireshark para comparar HTTP y HTTPS. Esta práctica es la base: cubre los protocolos y los filtros desde cero.

## 🧰 Herramientas

| Componente | Rol |
|---|---|
| Wireshark | Análisis gráfico de paquetes |
| tcpdump | Captura por línea de comandos |
| Red interna del laboratorio | Tráfico de práctica |

## ⚙️ Fases previstas

1. Capturar tráfico con `tcpdump` y guardarlo en un archivo `.pcap`.
2. Identificar el establecimiento de una conexión TCP.
3. Generar y analizar tráfico ARP, ICMP y DNS.
4. Aplicar filtros de captura y de visualización en Wireshark.
5. Reconstruir una conversación y comparar tráfico en texto plano con tráfico cifrado.

## 📋 Qué documentar

- Establecimiento de una conexión TCP
- Una consulta y respuesta DNS
- Filtros aplicados
- Diferencia entre texto plano y cifrado

## 🛡️ Buenas prácticas

- Los protocolos sin cifrado exponen su contenido a quien esté en la red.
- Segmentar la red y cifrar las comunicaciones reduce la exposición.

---
> ⚠️ Nota: se realiza únicamente en un entorno de laboratorio aislado propio (VirtualBox), con fines educativos.
