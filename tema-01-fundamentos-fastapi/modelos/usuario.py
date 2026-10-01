"""Modelo de datos para usuario.

Representa la estructura básica de un usuario dentro del sistema.
"""
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int | None = None
    nombre: str = ""
    correo: str = ""
