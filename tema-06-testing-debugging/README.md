# Tema 06 - Testing y Debugging

## Introducción

En cualquier proyecto de software, la capacidad de probar y depurar es lo que permite crecer sin romper la aplicación. Este tema enseña a detectar errores, crear pruebas y mantener la calidad del código.

## ¿Qué se aprende?

- Qué es un test en Python.
- Cómo probar endpoints con FastAPI.
- Cómo detectar errores con traceback y logs.
- Cómo validar comportamientos básicos antes de desplegar.

## Conceptos clave

### 1. Testing
El testing consiste en ejecutar validaciones automáticas para comprobar que el programa funciona como se espera.

### 2. Debugging
Debugging es el proceso de localizar, entender y corregir los errores del código.

### 3. TestClient
FastAPI incluye una forma de probar endpoints sin necesidad de iniciar un servidor manualmente.

### 4. Logs
Los logs ayudan a registrar eventos importantes, errores y mensajes del flujo de la aplicación.

## Buenas prácticas

- Crear pruebas pequeñas y específicas.
- Probar casos positivos y negativos.
- Revisar trazas de error detalladas.
- Mantener los logs claros y útiles.

## Estructura del tema

```text
tema-06-testing-debugging/
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

Este tema ayuda a construir software más confiable, entendible y seguro, con herramientas para validar cada cambio que haga el equipo.
