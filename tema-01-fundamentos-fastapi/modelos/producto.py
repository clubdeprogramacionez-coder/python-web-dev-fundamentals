"""Modelo de datos para producto.

Representa la estructura básica de un producto dentro del sistema.
"""
from dataclasses import dataclass

@dataclass
class Producto:
    id: int | None = None
    nombre: str = ""
    precio: float = 0.0
