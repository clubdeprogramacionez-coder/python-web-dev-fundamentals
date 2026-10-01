"""Endpoints relacionados con usuarios.

Este archivo sirve como plantilla para crear rutas de lectura,
creación y actualización de usuarios.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_usuarios():
    return []

@router.post("/")
async def crear_usuario():
    return {"mensaje": "Usuario creado"}
