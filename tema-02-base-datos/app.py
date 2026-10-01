"""Punto de entrada del Tema 02 - Base de Datos.

Este archivo representa la aplicación principal del tema.
"""
from fastapi import FastAPI

app = FastAPI(title="Tema 02 - Manejo de Base de Datos")

@app.get("/")
async def root():
    return {"mensaje": "API del tema 02 funcionando"}
