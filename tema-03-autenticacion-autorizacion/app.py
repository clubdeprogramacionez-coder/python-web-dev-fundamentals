"""Punto de entrada del Tema 03 - Autenticación y Autorización.

Este archivo sería el inicio de la API con rutas protegidas.
"""
from fastapi import FastAPI

app = FastAPI(title="Tema 03 - Autenticación y Autorización")

@app.get("/")
async def root():
    return {"mensaje": "API del tema 03 funcionando"}
