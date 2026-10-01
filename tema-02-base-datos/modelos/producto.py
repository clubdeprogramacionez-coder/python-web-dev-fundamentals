"""Modelo de datos para producto con base de datos.

Este modelo representa la tabla de productos que se guardará en la BD.
"""
from dataclasses import dataclass

@dataclass
class Producto:
    id: int | None = None
    nombre: str = ""
    precio: float = 0.0
