# Tema 03 - Autenticación y Autorización (JWT, OAuth)

## Introducción

La autenticación y la autorización son dos conceptos fundamentales en cualquier API. La autenticación confirma quién eres; la autorización determina qué puedes hacer.

## ¿Qué se aprende?

- Qué es OAuth2.
- Qué es JWT.
- Cómo generar tokens.
- Cómo proteger rutas con dependencias.
- Diferencia entre autenticación y autorización.

## Conceptos clave

### 1. Autenticación
Es el proceso por el cual el sistema valida la identidad del usuario. Por ejemplo, al verificar usuario y contraseña.

### 2. Autorización
Es la decisión sobre qué acciones puede realizar ese usuario dentro del sistema.

### 3. JWT
Un JWT es un token firmado que contiene información útil del usuario y puede ser verificado por el servidor.

### 4. OAuth2
OAuth2 es un estándar para la autorización de terceros y se usa ampliamente en APIs modernas.

## Buenas prácticas

- Nunca guardar contraseñas en texto plano.
- Usar variables de entorno para secretos.
- Configurar expiración en tokens.
- Proteger rutas sensibles con validaciones del rol.

## Estructura del tema

```text
tema-03-autenticacion-autorizacion/
├── app.py
├── requisitos.txt
├── README.md
├── core/
│   └── conexion_bd.py
├── controladores/
│   ├── usuarios_api.py
│   └── productos_api.py
└── modelos/
    ├── usuario.py
    └── producto.py
```

## Objetivo práctico

Este tema introduce la seguridad necesaria para APIs reales, donde no todos los usuarios pueden acceder a la misma información.
