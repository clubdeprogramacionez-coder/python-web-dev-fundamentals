"""Modelo de usuario para pruebas.

Representa la estructura basica de un usuario bajo validación.
"""
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int | None = None
    nombre: str = ""
    correo: str = ""
