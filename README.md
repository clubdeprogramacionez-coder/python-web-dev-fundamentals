# python-web-dev-fundamentals

Este repositorio contiene un curso práctico de desarrollo backend con Python y FastAPI, organizado por temas.

## Temas

- [Tema 01 - Fundamentos de FastAPI](./tema-01-fundamentos-fastapi/README.md)
- [Tema 02 - Manejo de Base de Datos (SQLAlchemy, SQL)](./tema-02-base-datos/README.md)
- [Tema 03 - Autenticación y Autorización (JWT, OAuth)](./tema-03-autenticacion-autorizacion/README.md)
- [Tema 06 - Testing y Debugging](./tema-06-testing-debugging/README.md)

## Objetivo general

El curso busca enseñar cómo construir APIs web robustas y escalables con Python, siguiendo buenas prácticas de organización, seguridad y pruebas.

## Estructura base que se repite por tema

Cada tema conserva la misma plantilla:

```text
tema-XX-nombre/
├── app.py
├── requisitos.txt
├── core/
│   └── conexion_bd.py
├── controladores/
│   ├── usuarios_api.py
│   └── productos_api.py
└── modelos/
    ├── usuario.py
    └── producto.py
```

La idea es que cada bloque temático tenga su propio README con contenido teórico y la estructura mínima del proyecto para empezar a practicar.
