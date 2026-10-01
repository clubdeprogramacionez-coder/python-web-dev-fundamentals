"""Modelo de datos para usuario con base de datos.

Este modelo representa la tabla de usuarios que se guardará en la BD.
"""
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int | None = None
    nombre: str = ""
    correo: str = ""
