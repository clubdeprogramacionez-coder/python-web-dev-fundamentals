"""Endpoints relacionados con usuarios para la base de datos.

Aquí se pueden crear rutas para listar o crear usuarios usando la BD.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_usuarios():
    return []

@router.post("/")
async def crear_usuario():
    return {"mensaje": "Usuario insertado"}
