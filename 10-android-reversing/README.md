# 10 · Seguridad Móvil en Android — Análisis, Reversing y Mitigación de Vulnerabilidades

**Objetivo:** aplicar ingeniería inversa sobre una aplicación Android vulnerable (InsecureBankv2) para comprender su funcionamiento interno, identificar debilidades de diseño y proponer medidas de mitigación.

**Herramientas:** APKTool · JADX-GUI · InsecureBankv2 · Kali Linux

## Metodología

1. **Decompilación con APKTool** — desensamblado de la APK objetivo (`apktool d InsecureBankv2.apk`), recuperando el `AndroidManifest.xml` legible y el bytecode Smali.
2. **Análisis estático con JADX-GUI** — conversión directa de bytecode `.dex` a código fuente Java de alta fidelidad, permitiendo inspeccionar clases críticas de la aplicación (`LoginActivity`, `ChangePassword`, `DoTransfer`, `CryptoClass`, entre otras).

## Hallazgos clave

- **Credenciales en SharedPreferences**: datos de usuario almacenados en un archivo identificable y legible en dispositivos con acceso root.
- **Ausencia de ofuscación**: nombres de clases, métodos y campos completamente legibles, exponiendo la lógica de negocio de forma inmediata.
- **Imports criptográficos visibles**: uso de `javax.crypto.*` y `android.util.Base64` auditable en detalle desde el código descompilado.
- **Control de flujo expuesto**: lógica condicional de privilegios (`is_admin`) visible y potencialmente manipulable.

## Recomendaciones de mitigación

- Ofuscación de código con **R8 / ProGuard**
- Gestión de secretos vía **Android Keystore System** (nunca embebidos en el código)
- Cifrado de datos locales con **AES-256-GCM** (`EncryptedSharedPreferences`)
- **Certificate Pinning** para prevenir ataques MitM
- **RASP** (Runtime Application Self-Protection) para detectar root, emuladores o modificaciones del APK
- Verificación de integridad con **Play Integrity API**

## Conclusiones

La ingeniería inversa con APKTool y JADX-GUI permite recuperar lógica de negocio crítica en minutos cuando una aplicación carece de ofuscación y protección de datos adecuada. La seguridad móvil efectiva requiere un modelo de defensa en profundidad: ofuscación, cifrado, protección de credenciales y detección en tiempo de ejecución (RASP).

> Práctica realizada en entorno de laboratorio aislado, con fines exclusivamente educativos, como parte del programa de Ciberseguridad de Tokio School.
