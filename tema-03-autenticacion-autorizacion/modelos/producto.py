"""Modelo de producto aplicado a la seguridad.

Aquí se puede relacionar cada producto con su propietario o permisos.
"""
from dataclasses import dataclass

@dataclass
class Producto:
    id: int | None = None
    nombre: str = ""
    propietario: str = ""
