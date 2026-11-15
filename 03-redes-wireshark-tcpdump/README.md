# Práctica 3 — Fundamentos de Redes y Análisis de Paquetes

| Nivel | Requisitos previos |
|---|---|
| 🟢 Básico | Prácticas 1 y 2 |

## 📌 Objetivo

Entender cómo viajan los datos por la red —establecimiento de una conexión TCP, una consulta DNS y una petición HTTP— capturando tráfico real con `tcpdump` y comparando una comunicación en texto plano con una cifrada (TLS).

## 🧰 Entorno y herramientas

| Componente | Detalle |
|---|---|
| Sistema | Ubuntu 24.04 LTS (contenedor Linux en la nube) |
| Herramientas | `tcpdump` 4.99.4, `openssl s_server`/`s_client`, servidor HTTP de prueba en Python |

> ⚠️ Nota de entorno: igual que la práctica 2, esta se ejecutó en un contenedor Linux en la nube, no en la VM de VirtualBox del resto del portafolio, y **sin interfaz gráfica**. Eso significa que no hay capturas de pantalla de Wireshark como en la práctica 13: todo el análisis se hizo con `tcpdump` en modo texto, que lee el mismo formato `.pcap` que Wireshark. Los tres archivos `.pcap` de la carpeta [`capturas/`](./capturas) se pueden abrir directamente en Wireshark para verlos de forma gráfica.

## ⚙️ Metodología

1. Captura del establecimiento de una conexión TCP (three-way handshake) y una petición HTTP en texto plano.
2. Captura del mismo tipo de comunicación pero cifrada con TLS, para comparar.
3. Captura de una consulta DNS real contra un dominio público.
4. Lectura de los tres `.pcap` en modo texto, con los filtros equivalentes a los que se usarían en Wireshark.

## 🔍 Desarrollo y resultados

### 1. Three-way handshake TCP y HTTP en texto plano

Captura: [`capturas/http-texto-plano.pcap`](./capturas/http-texto-plano.pcap)

```
$ tcpdump -i lo -w http-texto-plano.pcap -nn 'tcp port 9099'
# en paralelo: una petición GET a un servidor HTTP local
listening on lo, link-type EN10MB (Ethernet), snapshot length 262144 bytes
12 packets captured
```

Lectura del handshake (`tcpdump -r http-texto-plano.pcap -nn`):

```
23:19:18.405433 IP 127.0.0.1.50496 > 127.0.0.1.9099: Flags [S],  seq 84156503, ...
23:19:18.405448 IP 127.0.0.1.9099  > 127.0.0.1.50496: Flags [S.], seq 2128436383, ack 84156504, ...
23:19:18.405460 IP 127.0.0.1.50496 > 127.0.0.1.9099: Flags [.],  ack 1, ...
```

Esas tres líneas son el handshake completo: **SYN** (el cliente propone una secuencia), **SYN-ACK** (el servidor responde y confirma) y **ACK** (el cliente confirma). A partir de ahí la conexión queda establecida.

Con `-A` (volcado en ASCII), el contenido de la petición y la respuesta se lee sin ningún esfuerzo:

```
GET / HTTP/1.1
Accept-Encoding: identity
Host: 127.0.0.1:9099
User-Agent: Python-urllib/3.13
Connection: close

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.13.18
Content-type: text/html; charset=utf-8
...
<!DOCTYPE HTML>
<html lang="en">
```

**Nada de esto está oculto.** Cualquiera con acceso a la red — o, en este caso, cualquier proceso con permiso para capturar en la interfaz — puede leer la URL solicitada, las cabeceras y el cuerpo completo de la respuesta.

### 2. El mismo tráfico, pero cifrado (TLS)

Captura: [`capturas/https-cifrado.pcap`](./capturas/https-cifrado.pcap)

Se montó un servidor TLS de prueba con `openssl s_server` y un certificado autofirmado, y se repitió una petición equivalente con `openssl s_client`:

```
$ tcpdump -i lo -w https-cifrado.pcap -nn 'tcp port 9443'
16 packets captured
```

Al intentar leer el mismo tipo de paquete con `-A`:

```
23:19:33.863171 IP 127.0.0.1.34422 > 127.0.0.1.9443: Flags [P.], ..., length 293
E..Y..@.@............v$.w..q+{.....@.M.....
....c~.g.... .......5e.A_..f.t.S{. ./..,....'.c..f. Z....;.z....
```

No hay ningún texto legible: ni URL, ni cabeceras, ni contenido. Solo se distingue el handshake TLS (los paquetes iniciales, donde cliente y servidor negocian cifrado) y, después, bloques de `Application Data` opacos — la misma idea que documenta la práctica 13 sobre Apache, aquí comprobada con una captura propia.

### 3. Consulta DNS

Captura: [`capturas/dns.pcap`](./capturas/dns.pcap)

```
$ tcpdump -i eth0 -w dns.pcap -nn 'udp port 53'
$ getent hosts github.com
140.82.112.3    github.com

23:19:46.695976 IP 192.0.2.2.45365 > 8.8.8.8.53: 23198+ A? github.com. (28)
23:19:46.710128 IP 8.8.8.8.53 > 192.0.2.2.45365: 23198 1/0/0 A 140.82.112.3 (44)
```

Se ve la pregunta (`A? github.com`, pidiendo la dirección IPv4) y la respuesta (`A 140.82.112.3`). El número `23198` que aparece en ambas líneas es el identificador de la consulta: así el cliente sabe qué respuesta corresponde a qué pregunta. Igual que el HTTP sin TLS, **DNS tradicional viaja sin cifrar**: cualquiera en la ruta ve qué dominio se está resolviendo.

## 🎓 Lecciones aprendidas

- El three-way handshake (SYN, SYN-ACK, ACK) es la base de toda conexión TCP y se reconoce de inmediato en una captura por la combinación de flags.
- HTTP y DNS "clásicos" (sin TLS/DoH-DoT) exponen su contenido completo a quien capture el tráfico; TLS lo convierte en bytes opacos, aunque el handshake en sí sigue siendo visible.
- `tcpdump` en modo texto (`-A`, `-X`) permite el mismo análisis que Wireshark para quien no tiene entorno gráfico; los `.pcap` que genera son el mismo formato y se pueden abrir en Wireshark sin conversión.
- Capturar sin filtro en una interfaz real devuelve mucho ruido: aplicar el filtro correcto (`tcp port`, `udp port 53`) desde el principio ahorra tiempo de análisis.

---
> ⚠️ Nota: tráfico generado contra servicios propios de laboratorio (servidor HTTP y TLS locales) y una consulta DNS pública de ejemplo, con fines exclusivamente educativos. Los tres archivos `.pcap` no contienen información personal ni credenciales reales.
