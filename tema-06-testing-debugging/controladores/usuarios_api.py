"""Endpoints de prueba para usuarios.

Estos endpoints sirven como base para practicar validaciones y tests.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_usuarios():
    return []

@router.post("/")
async def crear_usuario():
    return {"mensaje": "Usuario validado"}
