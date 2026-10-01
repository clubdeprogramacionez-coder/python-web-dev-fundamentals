"""Endpoints para usuarios con autenticación.

Aquí podrían ir rutas protegidas de perfil y acceso basado en roles.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_usuarios_protegidos():
    return []

@router.post("/")
async def crear_usuario_protegido():
    return {"mensaje": "Usuario autenticado"}
