"""Endpoints relacionados con productos.

Este archivo funciona como plantilla para rutas de productos.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_productos():
    return []

@router.post("/")
async def crear_producto():
    return {"mensaje": "Producto creado"}
