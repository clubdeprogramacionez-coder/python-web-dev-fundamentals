"""Punto de entrada del Tema 01 - Fundamentos de FastAPI.

Este archivo debe ser el inicio de la aplicación.
"""
from fastapi import FastAPI

app = FastAPI(title="Tema 01 - Fundamentos de FastAPI")

@app.get("/")
async def root():
    return {"mensaje": "API del tema 01 funcionando"}
