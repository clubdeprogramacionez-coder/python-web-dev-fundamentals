"""Endpoints de prueba para productos.

Estos endpoints pueden usarse para verificar respuestas HTTP.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_productos():
    return []

@router.post("/")
async def crear_producto():
    return {"mensaje": "Producto validado"}
