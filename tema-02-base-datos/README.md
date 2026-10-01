# Tema 02 - Manejo de Base de Datos (SQLAlchemy, SQL)

## Introducción

En este tema se aprende a persistir datos en una base de datos relacional y a trabajar con consultas SQL o con un ORM como SQLAlchemy.

## ¿Qué se aprende?

- Qué es una base de datos relacional.
- Diferencia entre SQL y ORM.
- Cómo crear modelos para tablas.
- Cómo insertar, consultar, actualizar y eliminar registros.
- Qué son sesiones, transacciones y commits.

## Conceptos clave

### 1. Base de datos relacional
Una base de datos relacional organiza la información en tablas con filas y columnas. Esto permite guardar datos estructurados y relacionarlos entre sí.

### 2. SQL
SQL es el lenguaje estándar para consultar y manipular bases de datos. Permite crear tablas, insertar registros y filtrar información.

### 3. SQLAlchemy
SQLAlchemy es una librería de Python que permite interactuar con bases de datos usando clases y objetos, en lugar de escribir todo el SQL manualmente.

### 4. Sesión y transacción
La sesión es el punto de conexión entre la aplicación y la base de datos. La transacción agrupa operaciones que deben ejecutarse como una sola unidad.

## Buenas prácticas

- No mezclar la lógica de acceso a datos con los endpoints.
- Usar modelos claramente definidos.
- Cerrar sesiones adecuadamente.
- Mantener la conexión centralizada en `core`.

## Estructura del tema

```text
tema-02-base-datos/
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

La intención de este tema es preparar el proyecto para manejar datos reales, no solo objetos temporales en memoria.
