"""Endpoints para productos con autorización.

Estas rutas podrían requerir permisos especiales para administradores.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_productos_protegidos():
    return []

@router.post("/")
async def crear_producto_protegido():
    return {"mensaje": "Producto protegido"}
