"""Endpoints relacionados con productos para la base de datos.

Aquí se pueden crear rutas para consultar y guardar productos.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_productos():
    return []

@router.post("/")
async def crear_producto():
    return {"mensaje": "Producto insertado"}
