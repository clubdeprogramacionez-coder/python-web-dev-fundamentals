# Tema 01 - Fundamentos de FastAPI

## Introducción

FastAPI es un framework moderno para construir APIs web con Python. Está basado en estándares actuales y ofrece validación automática, documentación interactiva y un enfoque muy limpio para definir rutas y modelos de datos.

## ¿Qué se aprende en este tema?

- Crear una aplicación API desde cero.
- Definir rutas HTTP con `GET`, `POST`, `PUT`, `PATCH` y `DELETE`.
- Separar la lógica en capas: rutas, modelos y configuración.
- Entender la diferencia entre endpoint, controlador y modelo.
- Usar documentación automática con Swagger UI y Redoc.

## Conceptos clave

### 1. Aplicación principal
La aplicación se inicia con un objeto `FastAPI`. Ese objeto define el servidor de la API y registra los endpoints.

### 2. Endpoint
Un endpoint es una ruta HTTP asociada a una función. Por ejemplo:

- `GET /usuarios`
- `POST /usuarios`
- `GET /productos`

### 3. Modelo
Los modelos representan la estructura de datos. Podemos entenderlos como la forma que tendrán los objetos que manejamos dentro de la API.

### 4. Controlador
Un controlador agrupa las rutas relacionadas con un recurso, por ejemplo usuarios o productos.

### 5. Configuración central
La carpeta `core` guarda configuración general, por ejemplo la conexión a la base de datos o variables de entorno.

## Buenas prácticas

- Mantener cada recurso en su propio archivo.
- Evitar mezclar rutas, validaciones y lógica de negocio en un mismo archivo.
- Usar nombres claros para funciones y archivos.
- Documentar cada módulo con un README.

## Estructura del tema

```text
tema-01-fundamentos-fastapi/
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

Este tema sirve como base para todos los demás. Una vez que entiendas esta estructura, podrás expandir la API con autenticación, base de datos, pruebas y despliegue.
