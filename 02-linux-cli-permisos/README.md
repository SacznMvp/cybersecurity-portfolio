# Práctica 2 — Línea de Comandos de Linux y Permisos

| Nivel | Requisitos previos |
|---|---|
| 🟢 Básico | Práctica 1 |

## 📌 Objetivo

Dominar la terminal de Linux y el modelo de usuarios, grupos y permisos — unix (rwx, propietario/grupo, `umask`) — y usarlo para encontrar binarios SUID, una de las rutas más comunes de escalada de privilegios en Linux.

## 🧰 Entorno y herramientas

| Componente | Detalle |
|---|---|
| Sistema | Ubuntu 24.04 LTS (contenedor Linux en la nube) |
| Herramientas | Bash, `useradd`/`groupadd`, `chmod`, `chown`, `umask`, `find`, `su` |

> ⚠️ Nota de entorno: esta práctica se ejecutó en un contenedor Linux en la nube (Ubuntu 24.04), no en la VM de VirtualBox del resto del portafolio. El contenido y los resultados son equivalentes — es la misma distribución y las mismas herramientas —, pero no hay capturas de VirtualBox para esta práctica. Por eso tampoco existen `/var/log/auth.log` ni un servicio `rsyslog` persistente (ver sección 5): es una imagen mínima pensada para ejecutar comandos, no un sistema completo con journald/syslog.

## ⚙️ Metodología

1. **Navegación y manejo de archivos** — creación de una estructura de directorios de prueba y búsqueda de archivos con `find` y `grep`.
2. **Usuarios y grupos** — creación de usuarios y un grupo, y verificación en `/etc/passwd` y `/etc/group`.
3. **Permisos** — cambio de permisos en notación simbólica y octal, cambio de propietario, y efecto de `umask` sobre los archivos nuevos.
4. **Búsqueda de binarios SUID/SGID** — localización de los binarios SUID del sistema y demostración práctica de por qué ese bit es un riesgo.
5. **Logs de autenticación** — intento de revisión de `/var/log/auth.log` y constatación de que no existe en este entorno mínimo.

## 🔍 Desarrollo y resultados

### 1. Navegación y manejo de archivos

```
$ mkdir -p proyecto/{docs,scripts,logs} && cd proyecto
$ touch docs/informe.txt scripts/backup.sh logs/acceso.log
$ ls -la
total 20
drwxr-xr-x 5 root root 4096 nov 15 23:17 .
drwxr-xr-x 3 root root 4096 nov 15 23:17 ..
drwxr-xr-x 2 root root 4096 nov 15 23:17 docs
drwxr-xr-x 2 root root 4096 nov 15 23:17 logs
drwxr-xr-x 2 root root 4096 nov 15 23:17 scripts

$ find . -name "*.sh"
./scripts/backup.sh

$ echo "texto de prueba" > docs/informe.txt; grep -ril "prueba" .
./docs/informe.txt
```

### 2. Usuarios y grupos

```
$ groupadd equipo-seguridad
$ useradd -m -s /bin/bash -G equipo-seguridad analista1
$ useradd -m -s /bin/bash practicante

$ id analista1
uid=30033(analista1) gid=30033(analista1) groups=30033(analista1),30002(equipo-seguridad)

$ usermod -aG sudo analista1
$ groups analista1
analista1 : analista1 sudo equipo-seguridad

$ grep -E "^%sudo|^root" /etc/sudoers
root    ALL=(ALL:ALL) ALL
%sudo   ALL=(ALL:ALL) ALL
```

`analista1` queda en el grupo `sudo`, lo que —según la regla `%sudo ALL=(ALL:ALL) ALL` de `/etc/sudoers`— le da permiso para ejecutar cualquier comando como root mediante `sudo`. `practicante` se deja sin privilegios para la demostración siguiente.

### 3. Permisos: notación simbólica y octal

```
$ ls -l docs/informe.txt
-rw-r--r-- 1 root root 16 nov 15 23:17 docs/informe.txt

$ chmod u+x,g-w,o-r scripts/backup.sh && ls -l scripts/backup.sh
-rwxr----- 1 root root 0 nov 15 23:17 scripts/backup.sh

$ chmod 600 logs/acceso.log && ls -l logs/acceso.log
-rw------- 1 root root 0 nov 15 23:17 logs/acceso.log

$ chown analista1:equipo-seguridad docs/informe.txt && ls -l docs/informe.txt
-rw-r--r-- 1 analista1 equipo-seguridad 16 nov 15 23:17 docs/informe.txt
```

`backup.sh` queda legible y ejecutable solo por el propietario, y legible por el grupo (típico de un script compartido dentro de un equipo). `acceso.log` queda accesible solo por root, como corresponde a un archivo de auditoría.

### 4. `umask`

```
$ umask
0022
$ touch prueba-umask.txt && ls -l prueba-umask.txt
-rw-r--r-- 1 root root 0 nov 15 23:17 prueba-umask.txt

$ umask 027 && touch prueba-umask-027.txt && ls -l prueba-umask-027.txt
-rw-r----- 1 root root 0 nov 15 23:17 prueba-umask-027.txt
```

Con `umask 0022` (la base de un archivo es 666) un archivo nuevo queda en `644`. Con `umask 027`, más restrictivo, queda en `640`: el grupo no puede escribir y el resto del mundo no tiene ningún permiso.

### 5. Binarios SUID/SGID y escalada de privilegios

```
$ find / -xdev -perm -4000 -type f 2>/dev/null
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/su
/usr/bin/umount
```

Estos binarios son SUID por diseño (`passwd`, por ejemplo, necesita escribir en `/etc/shadow`, que solo root puede modificar). El riesgo aparece cuando un binario SUID *no estándar* —mal configurado, o puesto ahí por error o por un atacante— permite ejecutar código o abrir una shell. Para verlo en la práctica:

```
$ cp /usr/bin/bash /tmp/bash_suid_demo && chmod 4755 /tmp/bash_suid_demo
$ ls -l /tmp/bash_suid_demo
-rwsr-xr-x 1 root root 1446024 nov 15 23:17 /tmp/bash_suid_demo

$ su - practicante -c "/tmp/bash_suid_demo -p -c whoami"
root
```

**Hallazgo clave:** el usuario sin privilegios `practicante` ejecuta una copia de `bash` con el bit SUID activado (propiedad de root) y obtiene una shell con `whoami` = `root`. Es la demostración mínima de por qué un binario SUID fuera de lugar es una escalada de privilegios inmediata: no hace falta explotar ninguna vulnerabilidad de software, basta con que el permiso esté mal puesto.

El binario de prueba se eliminó al terminar (`rm -f /tmp/bash_suid_demo`); no queda ningún SUID adicional en el sistema.

### 6. Logs de autenticación

```
$ ls -la /var/log/auth.log
ls: cannot access '/var/log/auth.log': No such file or directory

$ su - noexiste -c "whoami"
su: user noexiste does not exist or the user entry does not contain all the required fields
```

Este contenedor no tiene `rsyslog`/`journald` corriendo, así que no genera `/var/log/auth.log`. En una máquina Ubuntu o Debian completa (como las VM del resto del portafolio), ese archivo sí existe y un intento de `su` fallido se vería con:

```
grep "Failed password\|authentication failure" /var/log/auth.log
```

## 🛡️ Mitigación

| Hallazgo | Medida |
|---|---|
| Un binario SUID fuera de lugar da root inmediato | Auditar periódicamente `find / -perm -4000` y eliminar/corregir cualquier SUID que no sea del sistema |
| `sudo` sin restricciones para todo el grupo `%sudo` | En producción, limitar por usuario y por comando en `/etc/sudoers.d/`, no dar `ALL=(ALL:ALL) ALL` a todo el grupo |
| `umask` por defecto (`022`) deja archivos legibles por todos | Usar `umask 027` o más estricto en servidores con datos sensibles |

## 🎓 Lecciones aprendidas

- El modelo de permisos de Linux es simple de leer (`rwx` × propietario/grupo/otros) pero un solo bit mal puesto —el SUID de este ejemplo— puede saltarse todo el modelo de privilegios.
- `umask` decide los permisos de cada archivo nuevo antes de que nadie lo configure a mano: vale la pena fijarlo explícitamente en servidores.
- Auditar binarios SUID es una revisión de pocos segundos (`find / -perm -4000`) que conviene automatizar con cron en un sistema real.
- No todos los entornos Linux tienen los mismos logs por defecto: antes de buscar evidencia de ataques hay que confirmar qué servicio de logging está activo.

---
> ⚠️ Nota: práctica realizada en un contenedor de laboratorio aislado con usuarios y datos ficticios, con fines exclusivamente educativos.
