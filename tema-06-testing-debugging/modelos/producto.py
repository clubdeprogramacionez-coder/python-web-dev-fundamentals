"""Modelo de producto para pruebas.

Representa la estructura básica de un producto a validar.
"""
from dataclasses import dataclass

@dataclass
class Producto:
    id: int | None = None
    nombre: str = ""
    precio: float = 0.0
