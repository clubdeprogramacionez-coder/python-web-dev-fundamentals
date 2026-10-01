"""Modelo de usuario para autenticación.

Representa una identidad con nombre de usuario y permisos.
"""
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int | None = None
    username: str = ""
    password_hash: str = ""
    rol: str = "usuario"
