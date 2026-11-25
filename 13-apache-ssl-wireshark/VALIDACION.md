# Validación TLS propuesta

**Estado: pendiente en VM.** La configuración es un ejemplo para el sitio estático del laboratorio, no una configuración universal de producción.

1. Registrar `apache2 -v`, `openssl version` y `curl --version`. Guardar snapshot y configuración anterior.
2. Crear un nuevo certificado de laboratorio con SAN en un directorio de trabajo privado. No sobrescribir la clave actual:

```sh
umask 077
openssl req -x509 -newkey rsa:2048 -nodes -days 30 -subj "/CN=sacznweb.local" -addext "subjectAltName=DNS:sacznweb.local" -keyout sacznweb.key -out sacznweb.crt
```

3. Tras revisar rutas y copias anteriores, instalar la clave con permisos restrictivos en `/etc/apache2/ssl/` y el certificado correspondiente. Conservar la confianza mediante un canal fiable; no aceptar cualquier certificado descargado de la red.
4. Habilitar `ssl` y `headers`, instalar la [configuración propuesta](config/sacznweb-ssl.conf) y habilitar el sitio. Ejecutar `apache2ctl configtest` antes de recargar. No añadir otro `Listen 443` si Ubuntu ya lo define en `ports.conf`.
5. Desde la propia VM, validar nombre y confianza explícita:

```sh
curl --resolve sacznweb.local:443:127.0.0.1 --cacert sacznweb.crt -v https://sacznweb.local/
curl --resolve sacznweb.local:443:127.0.0.1 --cacert sacznweb.crt --tlsv1.2 --tls-max 1.2 -v https://sacznweb.local/
curl --resolve sacznweb.local:443:127.0.0.1 --cacert sacznweb.crt --tlsv1.3 -v https://sacznweb.local/
```

6. Capturar en loopback con filtros `tcp.port == 443` y `tcp.port == 80`, realizar peticiones equivalentes y guardar capturas comentadas. Confirmar versión negociada en ServerHello y en curl. El backend TLS de curl debe soportar la versión solicitada.
7. Como prueba negativa, utilizar un certificado de confianza ajeno al servidor y comprobar que curl rechaza la conexión sin `-k`. Registrar el mensaje real.

Mantener HTTP habilitado solo durante la comparación aislada. Una ampliación posterior puede redirigir HTTP a HTTPS y evaluar HSTS, después de validar confianza y funcionalidad. El ejemplo no incluye HSTS para no interferir con este ejercicio.

| Validación | Resultado esperado | Observado |
|---|---|---|
| Confianza y SAN correctos | Conexión verificada y sitio accesible | Pendiente |
| Confianza incorrecta | Rechazo | Pendiente |
| TLS 1.2 / 1.3 | Negociación identificable en salida y captura | Pendiente |
| Comparación HTTP/HTTPS | Contenido HTTP visible; aplicación TLS cifrada | Pendiente |

Fuente: [Apache mod_ssl](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html).
